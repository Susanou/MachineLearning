Create view plain as
select word.mot as Mot, Themes.nom as Nom, frequences.frequence as Freq
from word, Themes, frequences
Where frequences.mot = word.id and frequencesword.theme = Themes.id;