# Sales Data Pipeline

Mini-projet Data Pipeline avec GitFlow.

## Structure GitFlow

- `main` : code stable en production
- `develop` : intégration des features validées
- `feature/*` : développements en cours
- `hotfix/*` : correctifs urgents

## Exécution du pipeline

```bash
pip install -r requirements.txt
python -m src.ingest data/sample_sales.csv > df
df = src.transform.transform(df)
src.load.load(df)

Diagramme ASCII GitFlow
main (stable prod)
│
│        merge PR
│       ---------->
develop (intégration features validées)
│
├── feature/add-sales-pipeline
│       │  commits fréquents
│       └─> PR → merge dans develop
│
├── feature/add-reporting
│       │  commits fréquents
│       └─> PR → merge dans develop
│
└── hotfix/fix-ingest-bug
        │  correction urgente
        └─> PR → merge dans main + develop
