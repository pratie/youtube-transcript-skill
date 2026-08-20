# Research a channel

**Prompt**

> What has @TED said about artificial intelligence? Read the three most
> relevant talks and compare their arguments.

**What the agent does**

1. Searches inside the channel instead of listing the whole archive:

```bash
curl -s "https://bulktranscripts.co/api/v1/channel/search?channel=@TED&q=artificial+intelligence&limit=10"
```

2. Picks the best candidates by title, then fetches only those transcripts
   (`segments=0` — quotes aren't needed for comparison):

```bash
curl -s "https://bulktranscripts.co/api/v1/transcript?video=VIDEO_ID&segments=0"
```

3. Compares the `paragraphs` of each and answers with per-video citations.

**Variants**

- Whole-archive audit: `GET /api/v1/channel/videos?channel=@TED&limit=1000`
  (1 credit), then fetch selectively.
- Topic discovery across all of YouTube: `GET /api/v1/search?q=...` — add
  `type=channel` to find channels worth following instead of videos.

**Cost note**: channel search costs 1 credit; each uncached transcript costs 1
credit; transcripts anyone has fetched before are free. Show the user the video
count before bulk-fetching.
