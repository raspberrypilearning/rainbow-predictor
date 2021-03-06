## Прогнозування веселки

Веселки з’являються, коли сонце світить крізь малесенькі крапельки води під правильним кутом (зазвичай після обіду). Якщо навколо тепло та волого, то варто перевірити, чи немає десь веселки.

+ Тепер давай будемо показувати веселку, тільки коли умови правильні. Зміни свій код таким чином:
    
    ![знімок екрана](images/rainbow-check.png)
    
    Ти не можеш бути повністю впевнений, що коли ці умови виконуватимуться, то обов’язково буде веселка, але перевірити варто.

+ Спробуй змінювати положення повзунка, поки не побачиш веселку.
    
    ![знімок екрана](images/rainbow-trigger.png)
    
    Пам’ятай, що отримані із датчиків значення не будуть точно такими ж, як на повзунках.

+ *Поріг* — це число, яке позначає якусь суттєву зміну. 20 градусів Цельсія та вологість 80% є пороговими значеннями для прогнозу веселки.
    
    Спробуй змінити порогові значення, а потім рухати повзунки, щоб отримати веселку.
    
    Якщо ти працюєш із справжнім Sense HAT, то ти можеш перевірити свій код, встановивши низькі порогові значення.