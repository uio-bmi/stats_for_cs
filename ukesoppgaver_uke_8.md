## Uke 8 oppgaver

**Oppgave 1.** Alice passerer fire trafikklys på vei til jobb, og hvert lys er like sannsynlig å være grønt eller rødt,
uavhengig av de andre.

  - Hvilken sannsynlighetsfordeling følger antall røde lys som Alice møter?
  - Hva er parameterne til denne fordelingen?
  - Hva er punktsannsynligheten, forventningsverdien og variansen til antall røde lys som Alice møter?
  - Anta at hvert rødt lys forsinker Alice med nøyaktig to minutter. Hva er variansen til Alices reisetid?

**Løsning.**
Antall røde lys som Alice møter følger en binomisk fordeling, siden hvert lys kan betraktes
som et Bernoulli-forsøk med to mulige utfall (rødt eller grønt), og forsøkene er uavhengige.
Parameterne til denne fordelingen er n = 4 (antall trafikklys) og p = 0.5 (sannsynligheten for å møte et rødt lys).
Punktsannsynligheten (PMF) til en binomisk fordeling er gitt ved:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
der k er antall suksesser (røde lys i dette tilfellet). For våre parametere blir punktsannsynligheten:
$$P(X = k) = \binom{4}{k} (0.5)^k (0.5)^{4-k} = \binom{4}{k} (0.5)^4$$

Forventningsverdien til en binomisk fordeling er gitt ved:
$$\mathbb{E}[X]= \sum_x xp_X(x) = np = 4 \cdot 0.5 = 2$$

Variansen til en stokastisk variabel X:
$$\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}[X])^2]=\sum_x (x-\mathbb{E}[X])^2 \cdot p_X(x)$$

Variansen til en binomisk stokastisk variabel forenkles til:
$$\text{Var}(X) = np(1-p) = 4 \cdot 0.5 \cdot 0.5 = 1$$

Hvis hvert rødt lys forsinker Alice med nøyaktig to minutter, kan den totale forsinkelsen uttrykkes som en stokastisk variabel Y = 2X, der X er antall røde lys. Variansen til Y kan beregnes ved hjelp av formelen for variansen til en lineær transformasjon av en stokastisk variabel:
$$\text{Var}(Y) = \text{Var}(2X) = 4 \cdot \text{Var}(X) = 4 \cdot 1 = 4$$
Dermed er variansen til Alices reisetid på grunn av røde lys 4 minutter i andre.

**Oppgave 2.** Temperaturen i en by er modellert som en stokastisk variabel med forventningsverdi og standardavvik begge lik 10 grader
Celsius. En dag beskrives som «normal» dersom temperaturen den dagen ligger innenfor ett standardavvik fra
forventningsverdien. Hva ville temperaturintervallet for en normal dag vært dersom temperaturen ble uttrykt i grader Fahrenheit?
Sammenhengen mellom Fahrenheit og Celsius: F = 1.8 * C + 32.

**Løsning.**
La den stokastiske variabelen X modellere temperaturen i grader Celsius. Vi kan da skrive:

$$\mathbb{E}[X] = 10$$
$$\sigma_X = 10 \Rightarrow \text{Var}[X] = 100$$

La Y være den stokastiske variabelen som modellerer temperaturen i grader Fahrenheit. Sammenhengen mellom X og Y er gitt ved:
$$Y = 1.8X + 32$$

Forventningsverdien til Y kan beregnes ved hjelp av lineariteten til forventningsverdien:
$$\mathbb{E}[Y] = \mathbb{E}[1.8X + 32] = 1.8 \mathbb{E}[X] + 32 = 1.8 \cdot 10 + 32 = 18 + 32 = 50$$

Variansen til Y:
$$\text{Var}(Y) = (1.8)^2 \text{Var}(X) = 3.24 \cdot 100 = 324$$

Og standardavviket til Y:
$$\sigma_Y = \sqrt{\text{Var}(Y)} = \sqrt{324} = 18$$

Temperaturintervallet for en normal dag i grader Fahrenheit ville vært mellom 32 og 68 grader Fahrenheit.

**Oppgave 3.** Anta at n personer kaster hattene sine i en eske, og deretter plukker hver person opp en hatt tilfeldig (hver hatt kan bare plukkes opp
av én person, og hver tildeling av hatter til personer er like sannsynlig). Hva er forventningsverdien til X, antallet
personer som får tilbake sin egen hatt? Merk at dette er den samme oppgaven som forrige uke, der løsningen ble
funnet gjennom simulering. I dette tilfellet skal du finne løsningen analytisk.

**Løsning.**
La $X_i$ være en indikator-stokastisk variabel som tar verdien 1 dersom den $i$-te personen får tilbake sin egen hatt, og 0 ellers,
og la X være det totale antallet personer som får tilbake sin egen hatt, dvs. $X = X_1 + X_2 + \ldots + X_n$.

Sannsynligheten for at hver person får tilbake sin egen hatt er $\frac{1}{n}$, siden det er n hatter og hver hatt er
like sannsynlig å bli plukket opp av enhver person:

$$P(X_i = 1) = \frac{1}{n} \quad \text{og} \quad P(X_i = 0) = 1 - \frac{1}{n}$$

Forventningsverdien til $X_i$ kan beregnes som følger:

$$\mathbb{E}[X_i] = 1 \cdot P(X_i = 1) + 0 \cdot P(X_i = 0) = \frac{1}{n}$$

Siden $X = X_1 + X_2 + \ldots + X_n$, kan vi bruke lineariteten til forventningsverdien for å finne forventningsverdien til $X$:

$$\mathbb{E}[X] = \mathbb{E}[X_1 + X_2 + \ldots + X_n] = \mathbb{E}[X_1] + \mathbb{E}[X_2] + \ldots + \mathbb{E}[X_n] = n \cdot \frac{1}{n} = 1$$

Dermed er det forventede antallet personer som får tilbake sin egen hatt lik 1.

**Oppgave 4.** I en by med en befolkning på 1 million mennesker er det vanligvis 10 virusinfeksjoner per dag. Historiske
data tyder på at infeksjoner oppstår tilfeldig og uavhengig med en konstant gjennomsnittlig rate. La X være antallet
infeksjoner som oppstår i løpet av en dag.

- Hvilken sannsynlighetsfordeling følger X?
- Hva er parameterne til denne fordelingen?
- Hva er punktsannsynligheten, forventningsverdien og variansen til X?
- Byen kunngjør en folkehelseadvarsel dersom antallet daglige infeksjoner overstiger forventningsverdi + 1 standardavvik. Over hvor mange infeksjoner bør en advarsel utstedes?
- Hva er sannsynligheten for at en advarsel utstedes på en gitt dag?

**Løsning.**

Antall infeksjoner som oppstår i løpet av en dag følger en Poisson-fordeling.
Parameterne til denne fordelingen er $\lambda = 10$ (gjennomsnittlig antall infeksjoner per dag).
Punktsannsynligheten (PMF) til en Poisson-fordeling er gitt ved:
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
der k er antall infeksjoner.

Forventningsverdien til en Poisson-fordeling er gitt ved:
$$\mathbb{E}[X] = \lambda = 10$$
Variansen til en Poisson-fordeling er også gitt ved:
$$\text{Var}(X) = \lambda = 10$$

Byen kunngjør en folkehelseadvarsel dersom antallet daglige infeksjoner overstiger forventningsverdi + 1 standardavvik. Terskelen for å utstede en advarsel er:
$$\text{Terskel} = \mathbb{E}[X] + \sigma_X = 10 + \sqrt{10} \approx 13.16$$
Derfor bør en advarsel utstedes dersom antallet infeksjoner overstiger 13.

Sannsynligheten for at en advarsel utstedes på en gitt dag er sannsynligheten for at antallet infeksjoner overstiger 13:
$$P(X > 13) = 1 - P(X \leq 13) = 1 - \sum_{k=0}^{13} \frac{10^k e^{-10}}{k!} \approx 0.13 $$

**Oppgave 5.** La X og Y være to stokastiske variabler med den gitte simultane punktsannsynligheten $p_{X,Y}$, og la $g$ og $h$ være
to funksjoner av henholdsvis $X$ og $Y$. Vis at dersom $X$ og $Y$ er uavhengige, så er de stokastiske variablene
$g(X)$ og $h(Y)$ også uavhengige.

**Løsning.**

La $U=g(X)$ og $V=h(Y)$. Da har vi:

$$p_{U,V}(u,v) = \sum_{\{(x,y) | g(x)=u,h(y)=v\}} p_{X,Y}(x,y)$$
$$=\sum_{\{(x,y) | g(x)=u,h(y)=v\}} p_X(x)p_Y(y)$$
$$=\sum_{\{x | g(x)=u\}} p_X(x) \sum_{\{y | h(y)=v\}} p_Y(y)$$
$$=p_U(u)p_V(v)$$