# sonarcloud-analysis
Integration of SonarCloud with GitHub for static code analysis in Python 

> Assignment | Software Development Security - COMPUTER SYSTEMS SECURITY – SECTION 20 – 2025 – 1

## Notas sobre la integración con SonarCloud

- El archivo `.github/workflows/sonarcloud.yml` fue actualizado siguiendo la documentación oficial de SonarScanner: [SonarScanner CLI](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner/).
- En las últimas versiones, SonarCloud provee por defecto el modo **Automatic Analysis** para nuevos proyectos (esta no puede ser utitilizada al mismo tiempo que SonarScanner CLI
).
- Existe una forma documentada y recomendada de utilizar SonarCloud en GitHub Actions mediante la [action oficial](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud).
- **En este caso, por motivos de tarea, se optó por corregir y actualizar el archivo `.yml` manualmente en vez de utilizar la solución oficial basada en la action.**

---

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=UVG-Works-Hub_sonarcloud-analysis&metric=alert_status&token=5ee7b630b805fa47e6e46aad41a01fc40dd83154)](https://sonarcloud.io/summary/new_code?id=UVG-Works-Hub_sonarcloud-analysis)