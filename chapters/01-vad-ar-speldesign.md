# Kapitel 1: Vad är speldesign?

## Varför detta kapitel finns

Det är lätt att blanda ihop en spelidé med speldesign. En idé kan vara “ett spel där man utforskar en ruin”, “ett snabbt rymdskjutspel” eller “ett pusselspel med ljusstrålar”. Men en idé säger inte tillräckligt mycket om vad spelaren faktiskt gör, vilka val som uppstår eller varför upplevelsen blir intressant.

Det här kapitlet ger ett grundspråk för resten av boken. Vi skiljer mellan idé, mekanik, regler, system och upplevelse. Målet är att du ska kunna titta på ett enkelt spel och se fler lager än bara temat eller implementationen.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara vad speldesign betyder i den här boken
- skilja mellan spelidé, mekanik, regel och spelupplevelse
- analysera ett enkelt spel utan att börja i kod eller spelmotor
- formulera en första designfråga för ett eget spelkoncept

## Innan vi börjar

Du har kanske redan byggt kopior av enkla spel. Då har du troligen tänkt på saker som objekt, kollisioner, input, poäng och uppdateringsloopar. Det är användbara tekniska byggstenar.

Speldesign ställer en annan sorts fråga:

Vad gör de tekniska byggstenarna med spelarens upplevelse?

En studsande boll är inte bara ett objekt med hastighet. I ett spel kan den vara hot, möjlighet, rytm, poängkälla eller stressmoment. Designperspektivet handlar om den betydelsen.

## Speldesign som formgivning av upplevelse

I den här boken använder vi ordet **speldesign** för arbetet med att forma spelets regler, mekaniker, mål, feedback och upplevelse.

Det betyder inte att speldesignern kontrollerar exakt vad spelaren känner. Spelare är olika. De kan tolka, ignorera, missförstå och använda spelet på oväntade sätt. Men designen skapar förutsättningar. Den gör vissa handlingar möjliga, vissa mål synliga och vissa beteenden mer sannolika.

En enkel formulering är:

Speldesign är att skapa ett system där spelaren kan agera, förstå konsekvenser och uppleva mening.

Den formuleringen innehåller tre viktiga delar:

- **System:** spelet har regler och relationer.
- **Handling:** spelaren kan göra något.
- **Mening:** handlingarna känns begripliga, intressanta eller värdefulla.

## Fyra lager i en spelidé

En spelidé kan förstås i flera lager. Vi börjar med fyra:

1. **Grundidé:** vad spelet verkar handla om.
2. **Mekaniker:** vad spelaren kan göra.
3. **Regler och system:** hur spelet reagerar och begränsar.
4. **Spelupplevelse:** vad spelaren faktiskt upplever.

Tänk på exemplet Skogsruinen.

Grundidén kan vara: “Spelaren utforskar en övergiven ruin i en skog.”

Det säger något om tema och miljö, men inte mycket om designen. Spelet kan bli långsamt och mystiskt, snabbt och farligt, taktiskt och resursdrivet eller socialt och samarbetsbaserat.

Om vi lägger till mekaniker blir bilden tydligare:

- spelaren kan gå mellan rum
- spelaren kan plocka upp nycklar
- spelaren kan öppna dörrar
- spelaren kan läsa symboler på väggar

Nu vet vi mer om vad spelaren gör. Men vi vet fortfarande inte hur svårt, riskfyllt eller meningsfullt det är.

Därför behövs regler och system:

- varje nyckel öppnar bara en viss typ av dörr
- vissa rum förändras när spelaren tar en nyckel
- facklor slocknar efter en viss tid
- symboler ger ledtrådar till säkra vägar

Nu börjar designen skapa val. Ska spelaren använda facklan nu eller spara den? Ska spelaren utforska ett sidrum eller gå direkt mot den låsta porten? Ska spelaren lita på symbolen?

Till sist får vi spelupplevelsen. Kanske känner spelaren nyfikenhet, osäkerhet, kontroll, stress eller belöning. Det är här designen möter människan.

## Mekanik: vad spelaren kan göra

En **mekanik** är en möjlig handling eller interaktion som spelaren kan använda eller påverkas av.

Exempel på mekaniker:

- hoppa
- sikta
- byta vapen
- samla resurser
- placera byggnader
- välja dialogalternativ
- kombinera föremål
- smyga förbi fiender

En mekanik är inte automatiskt intressant. Att kunna hoppa är i sig ganska enkelt. Det blir intressant när hoppandet sätts i relation till nivådesign, timing, risk, belöning och kontroll.

I ett plattformsspel kan hopp vara huvudmekanik. I ett rollspel kan hopp vara nästan irrelevant. I ett pusselspel kan hopp vara en regelbrytande specialförmåga. Samma handling får olika designbetydelse beroende på systemet runt omkring.

## Regler och system: vad handlingarna betyder

Regler avgör vad som händer när spelaren gör något. System är relationerna mellan flera regler.

Om spelaren kan plocka upp en nyckel är det en mekanik. Om nyckeln bara fungerar i dörrar med samma symbol är det en regel. Om valet av nyckel påverkar vilka rum som senare blir tillgängliga börjar vi se ett system.

För en utvecklare är det naturligt att tänka på system som teknisk logik. I speldesign tänker vi också på system som meningsskapare.

Ett system kan göra att spelaren tänker:

- “Jag borde spara den här resursen.”
- “Jag vågar inte gå dit än.”
- “Nu förstår jag vad symbolerna betyder.”
- “Om jag tar den snabba vägen missar jag kanske något viktigt.”

När regler leder till sådana överväganden har de börjat skapa designvärde.

## Spelupplevelse: vad spelaren faktiskt märker

**Spelupplevelse** är det spelaren faktiskt upplever när spelets regler, mekaniker, mål och feedback möts.

Det är viktigt att skilja mellan designerns avsikt och spelarens upplevelse.

Designerns avsikt kan vara: “Det här rummet ska kännas mystiskt.”

Spelarens upplevelse kan bli: “Jag förstår inte vad jag ska göra.”

Designerns avsikt kan vara: “Fienden ska skapa spänning.”

Spelarens upplevelse kan bli: “Kontrollen känns orättvis.”

Det betyder inte att designern misslyckas varje gång en spelare reagerar annorlunda än väntat. Men det betyder att speldesign behöver testas, observeras och justeras.

## Exempel: samma idé, olika design

Låt oss använda Skogsruinen igen.

### Version A: Pusselspel

Spelaren går mellan rum, läser symboler och placerar föremål i rätt ordning. Det finns ingen tidspress. Utmaningen är att förstå relationer.

Designfrågor:

- Är ledtrådarna tydliga men inte för uppenbara?
- Kan spelaren testa idéer utan att fastna permanent?
- Leder varje pussel till ett begripligt aha-ögonblick?

### Version B: Actionspel

Spelaren rör sig snabbt genom ruinen, undviker fällor och besegrar fiender. Nycklar och dörrar skapar tempo och risk.

Designfrågor:

- Känns kontrollen direkt och rättvis?
- Hinner spelaren läsa faror innan de träffar?
- Belönas mod utan att spelet blir slumpmässigt?

### Version C: Strategi- eller simulationsspel

Spelaren leder en expedition. Facklor, mat, utrustning och forskare är begränsade resurser. Ruinen är ett system att planera kring.

Designfrågor:

- Vilka resurser skapar mest intressanta val?
- Är konsekvenserna tillräckligt begripliga?
- Finns flera fungerande strategier?

Samma grundidé kan alltså bära helt olika spel. Det är designvalen, inte temat ensamt, som formar upplevelsen.

## Vanliga misstag

- **Misstag: Att börja med tema och tro att designen är klar.**
  - Varför det händer: Tema är lätt att föreställa sig och prata om.
  - Hur man undviker det: Skriv alltid ner vad spelaren gör, vilka regler som styr handlingen och vilken upplevelse du vill skapa.

- **Misstag: Att tänka på mekaniker som isolerade funktioner.**
  - Varför det händer: Utvecklare bygger ofta funktion för funktion.
  - Hur man undviker det: Fråga vad mekaniken betyder i relation till mål, risk, belöning och feedback.

- **Misstag: Att anta att spelaren upplever spelet som designern tänkt.**
  - Varför det händer: När man själv byggt spelet vet man redan hur det fungerar.
  - Hur man undviker det: Observera spelare utan att förklara för mycket. Notera vad de faktiskt förstår, gör och känner.

## Övningar

### Övning 1: Dela upp ett enkelt spel

Välj ett enkelt spel du känner väl, till exempel Snake, Tetris, Pong, Breakout eller ett enkelt mobilspel.

Skriv korta svar på följande:

1. Vad är spelets grundidé?
2. Vilka är tre centrala mekaniker?
3. Vilka regler gör mekanikerna meningsfulla?
4. Vilken upplevelse verkar spelet försöka skapa?

### Övning 2: Gör Skogsruinen till tre spel

Utgå från grundidén “spelaren utforskar en övergiven ruin i en skog”.

Beskriv kort hur idén skulle fungera som:

1. pusselspel
2. actionspel
3. strategispel eller simulation

För varje version: skriv en huvudmekanik och en önskad spelupplevelse.

### Fördjupning: Designfrågan

Formulera en designfråga för ett spel du själv vill skapa.

En bra designfråga kan börja så här:

- Hur får jag spelaren att känna ...?
- Vilka val ska spelaren göra när ...?
- Hur kan reglerna visa att ...?
- Vad ska spelaren förstå efter ...?

Exempel:

Hur får jag spelaren att känna nyfikenhet utan att göra nästa steg otydligt?

## Snabb sammanfattning

- En spelidé är inte samma sak som speldesign.
- Speldesign handlar om att forma regler, mekaniker, mål, feedback och upplevelse.
- En mekanik är något spelaren kan göra eller påverkas av.
- Regler och system avgör vad handlingarna betyder.
- Spelupplevelsen är det spelaren faktiskt upplever, inte bara det designern avsåg.
- Samma grundidé kan bli helt olika spel beroende på designval.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en grundidé och en mekanik?
2. Varför räcker det inte att säga att ett spel “handlar om att utforska en ruin”?
3. Hur kan samma mekanik få olika betydelse i olika genrer?
4. Vad är risken med att bara testa ett spel själv?
5. Vilken designfråga skulle du vilja undersöka i ett eget spel?

## Nästa steg

I nästa kapitel går vi vidare till spelarens mål och motivation. Om det här kapitlet handlade om vad spelet består av, handlar nästa om varför spelaren bryr sig om att fortsätta.
