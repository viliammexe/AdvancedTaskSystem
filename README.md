Advanced Task Management System (ATMS)
Tento repozitár obsahuje jednoduchý, ale modulárny systém na správu úloh implementovaný v jazyku Python. Projekt slúži ako referenčná vzorka pre testovanie a benchmarking algoritmov na detekciu podobnosti zdrojového kódu (napr. Jaccardov index, Winnowing algoritmus).

Architektúra systému
Projekt je rozdelený do niekoľkých logických modulov, aby demonštroval princípy čistej architektúry a oddelenia zodpovedností:

models.py: Definuje základné dátové štruktúry (CoreTask) využívajúce Python dataclasses.

engine.py: Obsahuje hlavnú biznis logiku pre spracovanie úloh, ich vytváranie a filtráciu podľa priority.

storage.py: Zabezpečuje perzistentné ukladanie dát do formátu JSON a prácu so súborovým systémom.

cli_interface.py: Modul určený na formátovanie a vizualizáciu dát v konzolovom prostredí (Dashboard).

main.py: Vstupný bod aplikácie, ktorý spája všetky moduly do funkčného celku.

Inštalácia a spustenie
Pre spustenie systému stačí mať nainštalovaný Python 3.7+ a spustiť hlavný skript:

Bash
# Klonovanie repozitára
git clone https://github.com/[TVOJE-MENO]/test-mining.git

# Spustenie aplikácie
python main.py
Účel testovania
Tento kód je špeciálne navrhnutý tak, aby obsahoval:

Typické programátorské konštrukcie: Triedy, metódy, podmienky a cykly.

Abstraktnú štruktúru: Vhodnú na testovanie AST (Abstract Syntax Tree) normalizácie.

Závislosti medzi súbormi: Na overenie schopnosti detekčného systému pracovať s importami a krížovými referenciami.

Tento projekt je súčasťou experimentálnej fázy vývoja systému na detekciu plagiátorstva v rámci bakalárskej práce na FEI TUKE.
