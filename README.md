# Appfollow test task

#### Instructions:

1. Download project dir
```bash
git clone ssad
```

2. Run docker-compose
```bash
cd appfollow_test
docker-compose build
docker-compose up -d
```

3. Open browser and visit
[http://127.0.0.1/posts](http://127.0.0.1/posts)

Crawler runs every hour by crontab
```bash
0 * * * * docker start crawler
```

To run the crawler manually, just run:
```bash
docker start crawler
```

### TODO:
- Add tests (pytest)
- Better error handling
