# YouTube Transcript Skill

An agent skill that gives Claude Code, Codex, Cursor and any SKILL.md agent
YouTube transcripts: one video, a playlist, or a whole channel of up to 1,000
videos in one bulk job. It also searches YouTube, searches inside one channel,
and tracks new uploads for free, through the
[BulkTranscripts](https://bulktranscripts.co) API.

**One free API key.** Sign in with Google at
[bulktranscripts.co/app?tab=mcp](https://bulktranscripts.co/app?tab=mcp), open
the **MCP & API** tab, and hit **Create key** in the **API keys** card. It is
free, with 30 credits included and no card. Every request carries that key. A one-time credit
pack tops up the same account, so the key keeps working; credits never expire,
and once a transcript is in your library you can re-read and re-export it for
free.

## Install

**skills CLI (Claude Code, Cursor, and friends)**

```bash
npx skills add pratie/youtube-transcript-skill
```

That installs the full skill plus the focused ones below; pick only what you
need with `--skill <name>`.

| Skill | Use it for |
| --- | --- |
| [youtube-transcripts](skills/youtube-transcripts/SKILL.md) | Everything in one skill: transcripts, search, channels, playlists, upload tracking |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | One video to clean text, timestamps, SRT/VTT or Markdown |
| [youtube-channel-transcripts](skills/youtube-channel-transcripts/SKILL.md) | Every video on a channel, or search inside one channel |
| [youtube-playlist-transcripts](skills/youtube-playlist-transcripts/SKILL.md) | A playlist or lecture series, in order |
| [youtube-search](skills/youtube-search/SKILL.md) | Find videos, channels or playlists, then read them |
| [youtube-upload-monitor](skills/youtube-upload-monitor/SKILL.md) | Free polling for new uploads, transcripts only for what is new |

The focused skills are generated from the full one by
`python3 scripts/build_skills.py`, so the API text stays identical everywhere.

**Claude Code**

```bash
mkdir -p ~/.claude/skills/youtube-transcripts
curl -fsSL https://bulktranscripts.co/skill.md \
  -o ~/.claude/skills/youtube-transcripts/SKILL.md
```

**OpenAI Codex**

```bash
mkdir -p ~/.codex/skills/youtube-transcripts
curl -fsSL https://bulktranscripts.co/skill.md \
  -o ~/.codex/skills/youtube-transcripts/SKILL.md
```

**OpenClaw** (published on [ClawHub](https://clawhub.ai/pratie/skills/bulktranscripts-youtube))

```bash
openclaw skills install @pratie/bulktranscripts-youtube
```

**Any SKILL.md-compatible agent:** copy [SKILL.md](skills/youtube-transcripts/SKILL.md) into your agent's
skills directory. Then set your key (required):

```bash
export BULKTRANSCRIPTS_API_KEY=bt_ak_your_key
```

## What it can do

| Capability | Cost |
|---|---|
| Fetch a video's transcript (clean text, paragraphs, timestamps) | 1 credit first time · your own repeat reads **free** |
| Fetch a whole channel or playlist as one background bulk job (up to 1,000 videos) | 1 credit per new transcript |
| Search YouTube for videos, channels, or playlists | 1 credit |
| Search inside one channel's uploads | 1 credit |
| List a channel's videos (up to 1,000) | 1 credit |
| List a playlist in order | 1 credit |
| Track a channel's newest uploads | **free** |

## Examples

- [Summarize a video](examples/summarize-video.md)
- [Research a channel](examples/research-channel.md)
- [Monitor a channel for new uploads](examples/monitor-channel.md)

## Prefer MCP?

The same engine is a hosted MCP server: no local process, ten tools, OAuth
sign-in. It works in Claude, Claude Code, Cursor and VS Code, and it is in
ChatGPT's plugin directory. Setup for each client is on the
[YouTube MCP server page](https://bulktranscripts.co/youtube-mcp-server); the
manifests live in [pratie/bulktranscripts-mcp](https://github.com/pratie/bulktranscripts-mcp).

```bash
claude mcp add --transport http bulktranscripts https://bulktranscripts.co/mcp
```

[Docs](https://bulktranscripts.co/docs) ·
[OpenAPI spec](https://bulktranscripts.co/openapi.json) ·
[Skill page](https://bulktranscripts.co/youtube-transcript-agent-skill) ·
[MCP server setup](https://bulktranscripts.co/youtube-mcp-server) ·
[YouTube transcript API](https://bulktranscripts.co/youtube-transcript-api) ·
[Pricing](https://bulktranscripts.co/#pricing)
