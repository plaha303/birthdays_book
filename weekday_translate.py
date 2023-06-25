def weekday_translate(day: str) -> str:
    english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ukrain = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

    index = english.index(day)
    translate = ukrain[index]

    return translate
