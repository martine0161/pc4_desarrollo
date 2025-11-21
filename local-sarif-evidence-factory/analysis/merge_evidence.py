import json
from pathlib import Path
from datetime import datetime

def load_json(filepath):
    """Carga JSON, retorna dict vacío si falla"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Error cargando {filepath}: {e}")
        return {}

def merge_evidence():
    base_path = Path(__file__).parent.parent / 'evidence'
    
    # Cargar evidencias
    sast = load_json(base_path / 'sast.json')
    sca = load_json(base_path / 'sca.json')
    sbom = load_json(base_path / 'sbom.json')
    
    # Crear reporte combinado
    combined = {
        'timestamp': datetime.now().isoformat(),
        'pipeline': 'local-sarif-evidence-factory',
        'summary': {
            'sast_issues': len(sast.get('results', [])),
            'sca_vulnerabilities': len(sca.get('dependencies', [])),
            'sbom_components': len(sbom.get('components', []))
        },
        'evidence': {
            'sast': sast,
            'sca': sca,
            'sbom': sbom
        }
    }
    
    # Guardar reporte
    output_path = base_path / 'combined_report.json'
    with open(output_path, 'w') as f:
        json.dump(combined, f, indent=2)
    
    print(f"✅ Reporte combinado guardado: {output_path}")
    print(f"📊 SAST issues: {combined['summary']['sast_issues']}")
    print(f"📊 SCA vulnerabilities: {combined['summary']['sca_vulnerabilities']}")
    print(f"📊 SBOM components: {combined['summary']['sbom_components']}")

if __name__ == '__main__':
    merge_evidence()