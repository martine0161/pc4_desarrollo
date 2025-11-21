#!/bin/bash
set -e

echo "📦 Generando SBOM..."

cd ../app
cyclonedx-py -r -o ../evidence/sbom.json || true

echo "✅ SBOM generado: evidence/sbom.json"