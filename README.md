# ETOS-AD – Adaptive Decision & Defense System

**ETOS-AD** er et eksperimentelt projekt der anvender **ETOS**-arkitekturen (baseret på M.E.M.-teorien) til at skabe et **selvlærende, forklarligt forsvarssystem** – med fokus på cybersikkerhed og adaptiv antivirus-beskyttelse.

## Kerneidé

ETOS kombinerer:
- **IDK** ("I Don't Know") – usikkerheds- og konfliktbaseret beslutningsmotor
- **CDP** – immutable forfatning / grundprincipper
- **Reflection Center** – post-beslutnings læring og justering

## Status (marts 2026)

- Teoretisk fundament (M.E.M.) → solid
- Beslutningsmotor (IDK/CDP) → ~70–80 % færdig
- Sikkerheds-adaptation → tidlig prototype-fase

## Mappe-struktur

```text
etos-ad/
├── core/                  # IKKE publiceret
├── security/
│   ├── security_mapper.py
│   └── security_etos_demo.py
├── .github/workflows/
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

## Sådan kører du demoen lokalt (midlertidig – kræver din egen IDK-motor)

1. Klon repoet:
git clone https://github.com/ditbrugernavn/etos-ad.git
cd etos-ad

2. Kopier din private `idk_engine.py` og `reflection_center.py` ind i en mappe kaldet `core/`

3. Kør demoen:
python security/security_etos_demo.py
