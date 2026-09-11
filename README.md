# YouTube Transcript Skill

Give your AI agent full YouTube access — transcripts, search (videos, channels,
playlists), search-inside-a-channel, playlist extraction, and free new-upload
tracking — via the [BulkTranscripts](https://bulktranscripts.co) API.

**One free API key.** Sign in with Google at
[bulktranscripts.co/app?tab=mcp](https://bulktranscripts.co/app?tab=mcp), open
the **Connect AI** tab, and hit **Create key** in the **API keys** card — free,
30 credits included, no card. Every request carries that key. A one-time credit
pack tops up the same account, so the key keeps working; credits never expire,
and once a transcript is in your library you can re-read and re-export it for
free.

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
skills directory. Then set your key (required):

```bash
export BULKTRANSCRIPTS_API_KEY=bt_ak_your_key
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
