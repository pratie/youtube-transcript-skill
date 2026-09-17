#!/usr/bin/env python3
"""Generate the focused skills in skills/ from skills/youtube-transcripts/SKILL.md.

skills/youtube-transcripts/SKILL.md is the single source of truth for the API text. Each focused
skill reuses its sections verbatim (auth, costs, the relevant endpoints, the
relevant error codes), so the copies cannot drift. Run after editing that file:

    python3 scripts/build_skills.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "skills" / "youtube-transcripts" / "SKILL.md").read_text()
body = src.split("---", 2)[2]


def between(start, end=None):
    i = body.index(start)
    j = body.index(end, i + len(start)) if end else len(body)
    return body[i:j].rstrip() + "\n"


AUTH = between("Base URL:", "## Costs")
COSTS = between("## Costs", "## Endpoints")
EP = {
    "transcript": between("### Get one transcript", "### Search YouTube"),
    "search": between("### Search YouTube", "### Search inside one channel"),
    "channel_search": between("### Search inside one channel", "### List a channel"),
    "channel_videos": between("### List a channel", "### List a playlist"),
    "playlist": between("### List a playlist", "### Newest uploads"),
    "latest": between("### Newest uploads", "### Balance"),
    "account": between("### Balance", "## Playbooks"),
}
errors_block = between("Errors come as", "Full reference:")
intro_err, *items = re.split(r"\n(?=- `)", errors_block.strip())
ERR = {re.match(r"- `(\w+)`", it).group(1): it for it in items}
COMMON_ERR = ["missing_api_key", "invalid_api_key", "invalid_input", "out_of_credits", "rate_limited"]

LINKS = (
    "[Docs](https://bulktranscripts.co/docs) ·\n"
    "[OpenAPI spec](https://bulktranscripts.co/openapi.json) ·\n"
    "[MCP server](https://bulktranscripts.co/youtube-mcp-server) ·\n"
    "[Free API key](https://bulktranscripts.co/app?tab=mcp)\n"
)

SKILLS = [
    dict(
        name="youtube-transcript",
        title="YouTube video transcript",
        desc="Get the transcript of a single YouTube video (or Short, or TikTok video) as clean text, timestamped segments, or SRT/VTT/Markdown via the BulkTranscripts API. Use when the user shares a video link and wants it summarized, quoted, translated, fact-checked or turned into notes. Requires a free BulkTranscripts API key in BULKTRANSCRIPTS_API_KEY, created at https://bulktranscripts.co/app?tab=mcp (Google sign-in, 30 free credits, no card).",
        lead="Fetch one video's transcript as clean text with metadata",
        eps=["transcript", "account"],
        errs=["no_transcript", "resolution_failed"],
        play="- **\"Summarize this video\"** → transcript with `segments=0`, then summarize\n  from `paragraphs`; cite the `title` and `url`.\n- **Quotes with timestamps** → keep `segments`, quote the text and link\n  `https://youtu.be/ID?t=START` for each one.\n- **Subtitles file** → `format=srt` or `format=vtt` returns the rendered file.\n",
    ),
    dict(
        name="youtube-channel-transcripts",
        title="Transcripts for a whole YouTube channel",
        desc="List every video on a YouTube channel (up to 1,000) and fetch their transcripts in bulk via the BulkTranscripts API, or search inside one channel for a topic. Use when the user wants all transcripts from a creator, a knowledge base or RAG corpus built from a channel, or research on what a creator has said. Requires a free BulkTranscripts API key in BULKTRANSCRIPTS_API_KEY, created at https://bulktranscripts.co/app?tab=mcp (Google sign-in, 30 free credits, no card).",
        lead="List a channel's videos, then pull the transcripts you need",
        eps=["channel_videos", "channel_search", "transcript", "account"],
        errs=["no_transcript", "resolution_failed"],
        play="- **Whole channel** → list videos first, show the user the count (each new\n  library transcript = 1 credit), then fetch transcripts one by one, skipping\n  failures (they are reported per video and refunded).\n- **Deep research on a creator** → `channel/search` for the topic, pick\n  candidates by title, fetch only those transcripts.\n",
    ),
    dict(
        name="youtube-playlist-transcripts",
        title="Transcripts for a YouTube playlist",
        desc="List a YouTube playlist in order and fetch the transcript of every video via the BulkTranscripts API. Use when the user shares a playlist link, wants a lecture series or course turned into study notes, or needs playlist transcripts as text. Requires a free BulkTranscripts API key in BULKTRANSCRIPTS_API_KEY, created at https://bulktranscripts.co/app?tab=mcp (Google sign-in, 30 free credits, no card).",
        lead="List a playlist in order, then pull each video's transcript",
        eps=["playlist", "transcript", "account"],
        errs=["playlist_private", "no_transcript", "resolution_failed"],
        play="- **Course or lecture series** → list the playlist, show the user the count\n  (each new library transcript = 1 credit), fetch transcripts in playlist\n  order with `segments=0`, skip failures (refunded), then build notes per video.\n",
    ),
    dict(
        name="youtube-search",
        title="YouTube search for agents",
        desc="Search YouTube for videos, channels or playlists, or search inside one channel, via the BulkTranscripts API, then fetch transcripts of the results. Use when the user asks to find videos about a topic, research what YouTube says about something, or locate a creator's videos on a subject. Requires a free BulkTranscripts API key in BULKTRANSCRIPTS_API_KEY, created at https://bulktranscripts.co/app?tab=mcp (Google sign-in, 30 free credits, no card).",
        lead="Search YouTube, then read the transcripts of what you find",
        eps=["search", "channel_search", "transcript", "account"],
        errs=["no_transcript", "resolution_failed"],
        play="- **Topic research** → search (1 credit), pick the most relevant results by\n  title and channel, fetch only those transcripts, then compare what they say\n  and cite each `title` and `url`.\n",
    ),
    dict(
        name="youtube-upload-monitor",
        title="Monitor YouTube channels for new uploads",
        desc="Check a YouTube channel's newest uploads for free via the BulkTranscripts API and fetch transcripts only for videos that are new. Use when the user asks what a channel posted recently, wants alerts or digests for new uploads, or wants to track competitors' channels. Requires a free BulkTranscripts API key in BULKTRANSCRIPTS_API_KEY, created at https://bulktranscripts.co/app?tab=mcp (Google sign-in, 30 free credits, no card).",
        lead="Poll channels for free, spend credits only on new videos",
        eps=["latest", "transcript", "account"],
        errs=["no_transcript", "resolution_failed"],
        play="- **\"What did X post this week?\"** → `channel/latest` (free), compare video\n  ids against what you have seen (use `published` when present), fetch\n  transcripts only for the relevant new videos.\n- **Recurring digest** → store the ids you have already handled; on each run\n  poll every channel, transcribe the new ids, summarize, and update the store.\n",
    ),
]

for sk in SKILLS:
    for key in ("name", "desc"):
        assert ": " not in sk[key], f"frontmatter-breaking colon in {sk['name']}"
    out = [
        "---",
        f"name: {sk['name']}",
        f"description: {sk['desc']}",
        "license: Proprietary API; this skill file is freely redistributable.",
        "---",
        "",
        f"# {sk['title']}",
        "",
        f"{sk['lead']}, using [BulkTranscripts](https://bulktranscripts.co).",
        LINKS,
        AUTH,
        COSTS,
        "## Endpoints",
        "",
    ]
    out += [EP[e] for e in sk["eps"]]
    out += ["## Playbook", "", sk["play"], intro_err, ""]
    out += [ERR[c] for c in sk["errs"] + COMMON_ERR]
    out += [
        "",
        "Need everything in one skill (transcripts, search, channels, playlists, monitoring)? Use the full",
        "[youtube-transcripts skill](https://github.com/pratie/youtube-transcript-skill).",
        "Full reference: [bulktranscripts.co/docs](https://bulktranscripts.co/docs)",
        "",
    ]
    d = ROOT / "skills" / sk["name"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text("\n".join(out))
    print("wrote", d.relative_to(ROOT) / "SKILL.md")
