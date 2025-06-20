Title: Отзыв на книгу "Architecture Patterns with Python"
Date: 2023-02-20
Category: books
Tags: architecture, great
Summary: База по DDD на питоне

![Cover]({static}cover.jpg){width=50%}

**TL/DR**: База по DDD на питоне

**Субъективная оценка**: 5/5

**Где взять**: [cosmicpython.com](https://www.cosmicpython.com/)

Читал для закрепления синей и красной книги по DDD, да и интересно посмотреть, как нынче модно модели делать. Понравилось, что в книге красивый современный питон и C4-диаграммы. После прочтения стало понятнее, что делают агрегаты - контролируют транзакционную целостность объектов, которые должны быть обновлены вместе + корень агрегата это более простая точка управления всем агрегатом. Еще в конце книги есть рекомендации, как пилить DDD, если у тебя Django - даже приятно, что обо мне подумали)

Инсайты:

- значения лучше заводить через датаклассы (потому что они сравниваются по полям вместо ID)
- сущности лучше делать через объекты, потому что они сравниваются через ID
- слой приложения занимается только оркестрацией, репозиторий только общением с базой, домен только логикой
  - сервисы добавляются после вытаскивания модели, когда вьюшка делает слишком много, иначе может случиться анемичная модель
- манкипатчинг это code smell, лучше подменять зависимости
  - патчи не драйвят улучшения дизайна
  - моки привязываются к деталям реализации
  - много моков переусложняют сетап тестов
  - testability == extensibility
- е2е тесты валидируют общую функциональность, тесты в домене позволяют увидеть проблемы кода
- лучше общаться с сервисным слоем на уровне примитивов, а не моделей домена (сервисный слой сам создаст нужные модели)
- агрегат ограничен транзакционной целостностью
  - единственный способ изменить часть агрегата это загрузить и сохранить его полностью
  - конкретная часть агрегата не адресуема снаружи
  - репозитории возвращают только агрегаты
  - референсы по ID вместо ссылок на объекты эффективно решают проблемы границ

![Mindmap]({static}mindmap.png){width=100% height=100%}
