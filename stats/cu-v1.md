# Component Usage Counts

Last updated: `2026-11-28T10:28:33Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 21209 |
| deploy | 15349 |
| upgrade | 5860 |

## By Component

| Name | Count |
|---|---:|
| docling | 1703 |
| embeddings | 614 |
| kokoro | 2753 |
| litellm | 559 |
| mcp | 740 |
| ollama | 606 |
| whisper | 13367 |
| whisperlive | 867 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 17012 |
| cuda | 4197 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 15099 |
| cuda | 4197 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 19118 |
| arm64 | 2039 |
| other | 52 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 6851 |
| `cu-v1-whisper-deploy-cpu-arm64` | 1180 |
| `cu-v1-whisper-deploy-cpu-other` | 2 |
| `cu-v1-whisper-deploy-cuda-amd64` | 1517 |
| `cu-v1-whisper-deploy-cuda-arm64` | 2 |
| `cu-v1-whisper-deploy-cuda-other` | 2 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 2335 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 293 |
| `cu-v1-whisper-upgrade-cpu-other` | 2 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 1179 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisper-upgrade-cuda-other` | 2 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 1623 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 40 |
| `cu-v1-kokoro-deploy-cpu-other` | 2 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 441 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 2 |
| `cu-v1-kokoro-deploy-cuda-other` | 2 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 445 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 21 |
| `cu-v1-kokoro-upgrade-cpu-other` | 2 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 171 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 2 |
| `cu-v1-kokoro-upgrade-cuda-other` | 2 |
| `cu-v1-docling-deploy-cpu-amd64` | 979 |
| `cu-v1-docling-deploy-cpu-arm64` | 180 |
| `cu-v1-docling-deploy-cpu-other` | 2 |
| `cu-v1-docling-deploy-cuda-amd64` | 201 |
| `cu-v1-docling-deploy-cuda-arm64` | 2 |
| `cu-v1-docling-deploy-cuda-other` | 2 |
| `cu-v1-docling-upgrade-cpu-amd64` | 211 |
| `cu-v1-docling-upgrade-cpu-arm64` | 23 |
| `cu-v1-docling-upgrade-cpu-other` | 2 |
| `cu-v1-docling-upgrade-cuda-amd64` | 97 |
| `cu-v1-docling-upgrade-cuda-arm64` | 2 |
| `cu-v1-docling-upgrade-cuda-other` | 2 |
| `cu-v1-mcp-deploy-cpu-amd64` | 497 |
| `cu-v1-mcp-deploy-cpu-arm64` | 46 |
| `cu-v1-mcp-deploy-cpu-other` | 2 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 176 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 17 |
| `cu-v1-mcp-upgrade-cpu-other` | 2 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 330 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 77 |
| `cu-v1-embeddings-deploy-cpu-other` | 2 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 185 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 18 |
| `cu-v1-embeddings-upgrade-cpu-other` | 2 |
| `cu-v1-litellm-deploy-cpu-amd64` | 327 |
| `cu-v1-litellm-deploy-cpu-arm64` | 51 |
| `cu-v1-litellm-deploy-cpu-other` | 2 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 161 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 16 |
| `cu-v1-litellm-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cpu-amd64` | 225 |
| `cu-v1-ollama-deploy-cpu-arm64` | 30 |
| `cu-v1-ollama-deploy-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cuda-amd64` | 121 |
| `cu-v1-ollama-deploy-cuda-arm64` | 2 |
| `cu-v1-ollama-deploy-cuda-other` | 2 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 101 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 7 |
| `cu-v1-ollama-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 110 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 2 |
| `cu-v1-ollama-upgrade-cuda-other` | 2 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 408 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 10 |
| `cu-v1-whisperlive-deploy-cpu-other` | 2 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 179 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 2 |
| `cu-v1-whisperlive-deploy-cuda-other` | 2 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 107 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 10 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 141 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 2 |
