# ETOS-AD – Adaptive Decision & Defense System

**ETOS-AD** er et eksperimentelt projekt der anvender **ETOS**-arkitekturen (baseret på M.E.M.-teorien) til at skabe et **selvlærende, forklarligt forsvarssystem** – med fokus på cybersikkerhed og adaptiv antivirus-beskyttelse.

## Kerneidé

ETOS kombinerer:
- **IDK** ("I Don't Know") – usikkerheds- og konfliktbaseret beslutningsmotor
- **CDP** – immutable forfatning / grundprincipper
- **Reflection Center** – post-beslutnings læring og justering

I denne adaptation flytter vi domænet fra etiske/sociale beslutninger → **endpoint-sikkerhed**:
- Konflikt mellem privatliv / brugervenlighed vs. trusselreduktion
- Usikkerhed i detektion (false positives, evasion, kontekst)
- Aggressivitet i respons (log-only vs. kill + isolate)

## Status (marts 2026)

- Teoretisk fundament (M.E.M.) → solid
- Beslutningsmotor (IDK/CDP) → ~70–80 % færdig (genbrugt fra etik-prototypen)
- Sikkerheds-adaptation → tidlig prototype-fase
- Reflection / læring → koncept + basal implementering

## Mappe-struktur

```text
etos-ad/
├── core/                  # IKKE publiceret – privat mappe / separat repo
│   ├── mem_theory.md
│   ├── idk_engine.py
│   ├── cdp.py
│   └── reflection_center.py
├── security/              # Her bygger vi antivirus-logikken
│   ├── security_mapper.py     # mapper events → IDK-parametre
│   └── security_etos_demo.py  # simpel loop med simulerede events
├── ui/                    # Flask + fremtidige dashboards
├── dirigent/              # PySide6 idé- og projektstyring (kopi eller submodule)
├── docs/                  # noter, use-cases, blockers
├── LICENSE
├── README.md
└── .gitignore
```

## Vigtig note om ejerskab

Kernen (M.E.M.-teorien + IDK/CDP/Reflection-motoren) er **Maria [dit efternavn]'s intellektuelle ejendom**.  
`/core`-mappen er **ikke** inkluderet i dette offentlige repo.  

Alt andet (sikkerheds-adaptation, demo-kode, UI-forslag) er MIT-licenseret.

## Licens

MIT (se LICENSE) – for alt udover `/core`.

## Næste trin (roadmap – tidlig 2026)

- [ ] Simuleret event-loop med realistiske trussel-scenarier
- [ ] Outcome-feedback → justering af IDK-vægte (uden CDP-brud)
- [ ] Integration med ETW / AMSI / fil-system watchers (Windows-fokus først)
- [ ] Minimal dashboard (divergence trends, emergency-rate, debt)
- [ ] YARA/heuristik som ekstra "regler"-input

Velkommen til at følge med, stille spørgsmål eller foreslå små forbedringer!
