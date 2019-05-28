
Create view plain as
select word.mot as Mot, themes.nom as Nom, frequences.frequence as Freq
from word, themes, frequences
Where frequences.mot = word.id and frequences.theme = themes.id;