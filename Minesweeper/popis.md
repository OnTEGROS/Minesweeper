Minesweeper je klasická hra designovaná Microsoftem v 90. letech.
Vykresluje 5 typy objektů:
    1. Zakryté políčko - políčko, na které lze kliknout pro jeho odkrytí a lze na něj položit vlaječku. V originálním Minesweeperovi má podobu vystínovaného šedého čtverce, který zobrazuje "vyvýšeninu" na poli.
    2. "Kliknuté" políčko - políčko na které hráč namířil a poté začal držet levé tlačítko. Pokud hráč levé tlačítko pustí nad stejným políčkem, provede se akce kliknutí levým tlačítkem.
    3. Odkryté políčko - pokud hráč klikne na zakryté políčko a neexploduje, políčko se odkryje. V originálním Minesweeperovi má podobu šedého čtverce s tmavšími okraji - více odkrytých políček vedle sebe tedy tvoří mřížku. Na odkrytém políčku se zobrazí číslo od 1 do 8 podle počtu min ve čtvercovém okruhu osmi políček odkrytého políčka. Pokud se v okruhu nenachází žádná mina, nezobrazí se na políčku žádné číslo.
    4. Časovač - hráči této hry rádi porovnávají časy za které stihnout vyřešit pole určité obtížnosti. V originálním Minesweeperovi má časovač jen 3 cifry a zasekne se na 999 sekundách.
    5. Počet min - jednoduché počítadlo zbývajících min. Jelikož miny nejdou odstranit, počítadlo začíná na původním počtu min, od kterého odečítá počet vlaječek které hráč položil. Pomocí počítadla lze někdy určit poloha některých min, pokud je jich dostatečně málo.
    6. Tlačítko start - Minesweeper hned při startu vytvoří novou hrací plochu, tlačítko funguje tedy jen pro restart hry. Na začátku nebo během hry zobrazuje tlačítko smiley face. Pokud je stisknuto uprostřed probíhající hry, hra se ukončí a vytvoří se nové hrací pole (možnost restartu uprostřed hry je důležitý například když víme, že máme mizerný čas a je zbytečné pokračovat ve hře). Pokud hráč exploduje, obliček na tlačítku se změní na zamračený s křížky místo očí, funkce tlačítka zůstává stejná - restart hry. Pokud hráč vyhraje, smiley face na tlačítku dostane sluneční brýle, tlačítko opět restartuje hru.
    7. "Kliknuté" tlačítko start - pokud hráč zmáčne a drží levé tlačítko myši nad tlačítkem start, začne se tlačítko jevit jako "zmáčknuté."

Při startu hry se vytvoří pole zakrytých políček, do kterých jsou po prvním tahu hráče náhodně umístěny miny.
Hráč může provádět jednu ze tří akcí:
    1. Kliknuté pravým tlačítkem - pokud hráč namíří na zakryté políčko a podrží pravé tlačítko myši (puštění pravého tlačítka nic neudělá), na pole se položí vlaječka. Vlaječky jsou určeny k položení tam, kde si hráč myslí, že se nacházi mina. Stejná akce na políčku s vlaječkou provede její odstranění.
   
    2. Kliknutí levým tlačítkem - pokud hráč namíří na políčko, stiskne a poté pustí levé tlačítko myši, políčko se pokusí odkrýt. Pokud je na políčku mina, hráč exploduje. Po explozi hra končí, hráč již nemůže na poli provádět žádné akce. Pokud na políčku mina není, pole se odkryje a ukáže počet min ve čtvercovém okruhu osmi políček okolo sebe. Pokud hráč na nějakém poli podrží levé tlačítko myši, poté z políčka myší sjede kamkoli jinam a poté tlačítko pustí, nestane se nic. 
    První odkrytí políčka levým kliknutím je první tah - ten rozmístí miny a spustí časovač.

    Pokud hráč přidrží levé tlačítko myši nad odkrytým políčkem, všechny políčka bez vlaječky v okruhu osmi políček okolo tohoto odkrytého políčka se změní na "kliknuté" políčka. Toto lze použít k snadnému vidění okruhu určitého políčka - aby hráč viděl všechny pole, kde se mina může potenciálně nacházet. Pokud je v okruhu osmi políček od odkrytého políčka s číslem stejný počet vlajek jako člslo na tomto políčku, hráč na políčko políčko klikne levým tlačítkem myši a poté tlačítko pustí, všechny políčka v okruhu osmi políček okolo odkrytého políčka se pokusí odkrýt. Pokud hráč správně položil vlaječky v okruhu políčka, všechny políčka v okruhu se úspěšně odkryjí. Pokud ne, exploduje.
    Opět, pokud hráč přidrží levé tlačítko myši nad odkrytým políčkem a poté tlačítko pustí nekde jinde, nic se nestane.
    Klikání na odkrytá políčka není nutné ke zvládnutí hry, slouží jen jako urychlení abychom nemuseli klikat vícekrát pokud již víme, kde se nachází miny v okruhu určitého políčka.

    3. Kliknutí levým tlačítkem na tlačítko start a následné puštění levého tlačítka stále nad tlačítkem start - restart hry.
   
Podmínka pro výhru hry je odkrytí všech políček, na kterých není mina.
První tah hráče nikdy nemůže být exploze - miny jsou rozmístěny až po odkrytí prvního políčka.
Pokud hráč odkryje pokíčko, které ve svém okruhu nemá žádnou minu, jsou automaticky odkryty i všechna políčka v okruhu tohoto odkrytého políčka. To může spustit řetězovou reakci, kde pokud je tímto procesem odkryto další políčko bez miny ve svém okruhu, také odkryje všechna políčka ve svém okruhu. Toto se hráči jeví jako "odkrytí velké plochy jedním kliknutím."

První tah právě často odkryje velkou plochu jedním kliknutím. Pokud se prvím tahem odkryje jen jedno políčko, obvykle hru restartujeme, protože nemáme dostatek prostoru na to, abychom určili kde se miny nachází.

Nejklasičtější a nejjednodušší situace ve hře je jednička v rohu. Je to situace, kdy máme odkryté políčko, které ukazuje "1", a které má ve svém okruhu jen jedno zakryté políčko. Je tedy jasné, že jediné políčko, kde může být mina, je to jediné v okruhu. Odkryté políčko s číslem, v jehož okruhu jsme našli všechny miny, je "vyřešené." 
Pokud tedy máme dvě jedničky vedle sebe, z nichž jedna je v rohu, můžeme vyřešit jedničku v rohu, což vyřeší i jedničku vedle ní, protože už budeme mít splněn počet min v jijím okruhu.
Situace je popsána v "1.png", "2.png" a "3.png"