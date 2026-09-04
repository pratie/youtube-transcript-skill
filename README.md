# YouTube Transcript Skill

Give your AI agent full YouTube access — transcripts, search (videos, channels,
playlists), search-inside-a-channel, playlist extraction, and free new-upload
tracking — via the [BulkTranscripts](https://bulktranscripts.co) API.

**No signup.** The skill works immediately on the free tier (30 transcript
additions, limited by device and public IP). A one-time credit pack's license
key unlocks more; credits never expire, and once a transcript is in your
library you can re-read and re-export it for free.

## Install

**skills CLI (Claude Code, Cursor, and friends)**

```bash
npx skills add pratie/youtube-transcript-skill
```

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

**Any SKILL.md-compatible agent** — copy [SKILL.md](SKILL.md) into your agent's
skills directory. With purchased credits, set:

```bash
export BULKTRANSCRIPTS_API_KEY=your_license_key
```

## What it can do

| Capability | Cost |
|---|---|
| Fetch a video's transcript (clean text, paragraphs, timestamps) | 1 credit first time · your own repeat reads **free** |
| Search YouTube — videos, channels, or playlists | 1 credit |
| Search inside one channel's uploads | 1 credit |
| List a channel's videos (up to 1,000) | 1 credit |
| List a playlist in order | 1 credit |
| Track a channel's newest uploads | **free** |

## Examples

- [Summarize a video](examples/summarize-video.md)
- [Research a channel](examples/research-channel.md)
- [Monitor a channel for new uploads](examples/monitor-channel.md)

## Prefer MCP?

The same engine is a hosted MCP server — no local process, seven tools:

```bash
claude mcp add --transport http bulktranscripts https://bulktranscripts.co/mcp
```

Docs: https://bulktranscripts.co/docs · OpenAPI: https://bulktranscripts.co/openapi.json
· Skill page: https://bulktranscripts.co/youtube-transcript-agent-skill
