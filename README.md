# ETOS-AD – Adaptive Decision & Defense System

**ETOS-AD** er en offentlig prototype, der demonstrerer hvordan ETOS-arkitekturens beslutningslogik kan bruges i en cybersikkerheds-kontekst.

Projektet viser en lille, forklarlig sikkerhedsadapter, som oversætter events til spændinger (*tensions*) og evaluerer dem gennem en demo-motor. Den private kerne bag ETOS er **ikke** inkluderet i dette repository.

## Hvad repoet indeholder

- `security/security_mapper.py` – oversætter sikkerheds-events til ETOS/IDK-lignende tensions på en 0–5 skala
- `security/security_etos_demo.py` – kørbar demo, inkl. placeholder-motor hvis den private kerne ikke er til stede
- `tests/` – enkle tests for mapping og smoke test af demoen
- `.github/workflows/ci.yml` – simpel CI, der kører syntax check og tests

## Arkitekturstatus

- **M.E.M.-teoretisk fundament**: etableret
- **ETOS-beslutningslag**: intern udvikling
- **Sikkerhedsadapter / demo**: offentlig prototype

## Mappe-struktur

```text
ETOS-antivirus/
├── .github/
│   └── workflows/
│       └── ci.yml
├── security/
│   ├── __init__.py
│   ├── security_etos_demo.py
│   └── security_mapper.py
├── tests/
│   ├── test_security_demo_smoke.py
│   └── test_security_mapper.py
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

## Lokal kørsel

```bash
python -m pip install -r requirements.txt
python security/security_etos_demo.py --once --sleep 0
```

Hvis du har en privat ETOS-kerne lokalt, kan du lægge den i `core/` med fx `idk_engine.py`.
Hvis ikke, bruger demoen automatisk en placeholder-motor, så repoet stadig kan køres og testes.

## Test

```bash
pytest -q
```

## Bemærkning

Dette repository er en **offentlig demo/prototype**. Det repræsenterer ikke den fulde ETOS-kernelogik, M.E.M.-teoriens komplette implementering eller den interne governance-motor.
