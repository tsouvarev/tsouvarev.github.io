Title: Отзыв на книгу "Secure by Design"
Date: 2024-02-22
Category: books
Tags: architecture, ddd, great
Summary: Если сразу писать код по бест-практис, то будет еще и безопаснее

![Cover]({static}cover.jpg){width=50%}

**TL/DR**: Если сразу писать код по бест-практис, то будет еще и безопаснее

**Субъективная оценка**: 5/5

**Где взять**: [Manning](https://www.manning.com/books/secure-by-design)

Начал читать, потому что думал, что книга про хардкорные штуки от безопасников, но оказалось, что она про принципы дизайна кода, которые позволяют избежать базовых проблем с безопасностью. Еще абсолютно неожиданно авторы много внимания уделяют DDD и хорошо мотивируют делать классные доменные модели, так что рекомендую в рамках осознания DDD.

Инсайты:

- авторы толкают очень симпатичный тейк про то, что за счет дизайна можно порешать многие проблемы с безопасностью. но больше всего рассказывают, про то, как доменные примитивы помогают бороться с невалидным инпутом и неконсистентным стейтом внутри слоя домена
- часто упоминают ограниченные контексты из DDD и маппинг сущностей, есть примеры того, как из-за отсутствия маппинга были жесткие баги
- есть отдельная глава про рефакторинг легаси, чтобы он стал более безопасным, но там без удивительных открытий - потихоньку добавлять примитивы, ограничивать контексты
- интересная мысль про то, что DRY это не про непосредственно код, а про некоторое знание, которое этот код выражает. Поэтому бывают кейсы, когда одинаковый код это не повторение, и когда разный код очень даже повторение. Я тоже часто пользовался таким объяснением, но не так четко выражал
- есть глава про распил монолита, но там тоже все довольно стандартное

![Mindmap]({static}mindmap.png){width=100% height=100%}
