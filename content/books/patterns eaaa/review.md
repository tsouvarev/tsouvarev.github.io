Title: Отзыв на книгу "Patterns of Enterprise Application Architecture"
Date: 2023-10-22
Category: books
Tags: architecture, good
Summary: Классический справочник по архитектурным паттернам

![Cover]({static}cover.jpg){width=50%}

**TL/DR**: Классический справочник по архитектурным паттернам

**Субъективная оценка**: 4/5

**Где взять**: [Amazon](https://www.amazon.com/Patterns-Enterprise-Application-Architecture-Martin/dp/0321127420)

Начал читать, потому что с рефакторингом приходится принимать много решений по внутреннему устройству и пытаюсь найти источник, где давались бы нужные мне ответы (понятно, что идеального ответа не будет, но все же) - что должно быть в доменной модели, как очертить границы, где их можно нарушать, нужны ли DTO, можно ли везде заюзать pydantic и тд. Сама книга построена в формате справочника по паттернам + глава, где они все связываются между собой. Много примеров на Java и C#.

Инсайты:

- Java просто уникально многословная, из-за этого сложно понять, что происходит на трех страницах подряд с фабриками, интерфейсами и интерфейсами фабрик. Gри этом с С# полегче. Еще в ч/б нет подсветки, грустно
- книга 2002 года, так что многие вещи устарели - я даже не стал заносить в майндмап тему про mvc и сессии. Половина штук воспринимается как данное по умолчанию, еще четверть вообще непонятно для кого, остальное норм (но мб это у меня сейчас линза восприятия такая и еще не столкнулся с описанными проблемами)
- местами у общепринятых терминов другая интерпретация (например, у DTO или репозитория). но тут сложно винить автора, за будущее он не в ответе
- не везде понятна разница между паттернами (я бы еще погуглил разницу между гейтвеями и table module)
- активно пиарит unit of work, при этом иронично, что все крупные фреймворки в итоге выбрали active record (как у Django и Ruby on rails)
- не смотря на то, что есть глава с нарративами, лично мне не хватило вписывания паттернов в ландшафт решений. У каждого паттерна есть куча кода с реализацией, но нет явных сценариев и сцепок с другими паттернами (где просто словами бы объяснили что происходит)
- интересная глава с локами

![Mindmap]({static}mindmap.png){width=100% height=100%}
