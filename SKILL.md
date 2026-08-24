---
name: youtube-transcripts
description: Fetch YouTube video transcripts, search YouTube, list channel or playlist videos, and track new uploads via the BulkTranscripts API. Use when the user shares a YouTube link, asks to summarize/analyze/quote a video, wants transcripts for a whole channel or playlist, needs YouTube research, or asks what a channel posted recently. Works immediately with no API key (free tier); set BULKTRANSCRIPTS_API_KEY for purchased credits.
license: Proprietary API; this skill file is freely redistributable.
---

# YouTube transcripts via BulkTranscripts

Base URL: `https://bulktranscripts.co`

All endpoints are plain GET returning JSON. Keyless calls draw from a free
allowance (30 transcripts per public IP). If `BULKTRANSCRIPTS_API_KEY` is set,
send it on every request:

```bash
curl -s "https://bulktranscripts.co/api/v1/..." \
  ${BULKTRANSCRIPTS_API_KEY:+-H "Authorization: Bearer $BULKTRANSCRIPTS_API_KEY"}
```

## Costs (check `billing.remaining` in every response)

- Transcript: 1 credit — **cached transcripts are FREE**, so always try before assuming cost
- Search / channel videos / playlist videos: 1 credit each
- `channel/latest` and `account`: always free
- Failures (no captions, video unreachable) are auto-refunded, never charged

When a call returns HTTP 402 `out_of_credits`, tell the user their free
allowance/credits are used up and link them to
https://bulktranscripts.co/#pricing (one-time packs; the license key from
checkout is the API key).

## Endpoints

### Get one transcript
```bash
curl -s "https://bulktranscripts.co/api/v1/transcript?video=VIDEO_URL_OR_ID"
```
Params: `video` (watch URL, youtu.be, Shorts, bare 11-char id, or TikTok video
URL) · `language` (default `en`) · `segments=0` to omit timestamps (smaller) ·
`format=txt|md|srt|vtt|csv|ai` to get a rendered file instead of JSON ·
`fresh=1` to force re-extraction.

Response fields: `title`, `channel`, `duration`, `upload_date`, `language`,
`source` (manual_caption|auto_caption), `cached`, `word_count`, `text`,
`paragraphs[]` (silence-grouped — best for reading/chunking), `segments[]`
(`{text, start, duration}`), `billing`.

Long videos produce long text. For summarization, prefer `segments=0` and read
`paragraphs`.

### Search YouTube (1 credit)
```bash
curl -s "https://bulktranscripts.co/api/v1/search?q=QUERY&limit=10"
```
Add `type=channel` or `type=playlist` to search for channels/playlists instead
of videos.

### Search inside one channel (1 credit)
```bash
curl -s "https://bulktranscripts.co/api/v1/channel/search?channel=@HANDLE&q=TOPIC&limit=10"
```
Finds a creator's videos about a topic without listing the whole archive.

### List a channel's videos (1 credit, up to 1000)
```bash
curl -s "https://bulktranscripts.co/api/v1/channel/videos?channel=@HANDLE&limit=100"
```
`channel` accepts @handle, channel URL, or UC… id.

### List a playlist in order (1 credit)
```bash
curl -s "https://bulktranscripts.co/api/v1/playlist/videos?playlist=PLAYLIST_ID_OR_URL"
```

### Newest uploads — FREE, use for monitoring
```bash
curl -s "https://bulktranscripts.co/api/v1/channel/latest?channel=@HANDLE"
```
Returns up to 15 recent videos with `published` timestamps. Poll this freely;
only spend credits on videos that are actually new.

### Balance
```bash
curl -s "https://bulktranscripts.co/api/v1/account"
```

## Playbooks

- **"Summarize this video"** → transcript with `segments=0`, then summarize
  from `paragraphs`; cite the `title` and `url`.
- **Whole channel/playlist** → list videos first, show the user the count
  (each uncached transcript = 1 credit), then fetch transcripts one by one,
  skipping failures (they are reported per video and refunded).
- **"What did X post this week?"** → `channel/latest` (free), compare
  `published` dates, fetch transcripts only for the relevant new videos.
- **Deep research on a creator** → `channel/search` for the topic (or list all
  videos), pick candidates by title, fetch only those transcripts.

Errors come as `{"error": {"code", "message"}}` — `no_transcript` means the
video has no captions (not charged); `invalid_input` means a malformed
URL/id. Full reference: https://bulktranscripts.co/docs
