# Component Usage Counts

Last updated: `2026-07-11T21:06:15Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 586 |
| deploy | 390 |
| upgrade | 196 |

## By Component

| Name | Count |
|---|---:|
| docling | 31 |
| embeddings | 21 |
| kokoro | 58 |
| litellm | 48 |
| mcp | 29 |
| ollama | 26 |
| whisper | 330 |
| whisperlive | 43 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 461 |
| cuda | 125 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 363 |
| cuda | 125 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 553 |
| arm64 | 33 |
| other | 0 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 132 |
| `cu-v1-whisper-deploy-cpu-arm64` | 17 |
| `cu-v1-whisper-deploy-cpu-other` | 0 |
| `cu-v1-whisper-deploy-cuda-amd64` | 55 |
| `cu-v1-whisper-deploy-cuda-arm64` | 0 |
| `cu-v1-whisper-deploy-cuda-other` | 0 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 74 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 6 |
| `cu-v1-whisper-upgrade-cpu-other` | 0 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 46 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisper-upgrade-cuda-other` | 0 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 37 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 0 |
| `cu-v1-kokoro-deploy-cpu-other` | 0 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 7 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 0 |
| `cu-v1-kokoro-deploy-cuda-other` | 0 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 13 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cpu-other` | 0 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 0 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 0 |
| `cu-v1-kokoro-upgrade-cuda-other` | 0 |
| `cu-v1-docling-deploy-cpu-amd64` | 26 |
| `cu-v1-docling-deploy-cpu-arm64` | 1 |
| `cu-v1-docling-deploy-cpu-other` | 0 |
| `cu-v1-docling-deploy-cuda-amd64` | 1 |
| `cu-v1-docling-deploy-cuda-arm64` | 0 |
| `cu-v1-docling-deploy-cuda-other` | 0 |
| `cu-v1-docling-upgrade-cpu-amd64` | 3 |
| `cu-v1-docling-upgrade-cpu-arm64` | 0 |
| `cu-v1-docling-upgrade-cpu-other` | 0 |
| `cu-v1-docling-upgrade-cuda-amd64` | 0 |
| `cu-v1-docling-upgrade-cuda-arm64` | 0 |
| `cu-v1-docling-upgrade-cuda-other` | 0 |
| `cu-v1-mcp-deploy-cpu-amd64` | 14 |
| `cu-v1-mcp-deploy-cpu-arm64` | 0 |
| `cu-v1-mcp-deploy-cpu-other` | 0 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 10 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 5 |
| `cu-v1-mcp-upgrade-cpu-other` | 0 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 13 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 1 |
| `cu-v1-embeddings-deploy-cpu-other` | 0 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 7 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 0 |
| `cu-v1-embeddings-upgrade-cpu-other` | 0 |
| `cu-v1-litellm-deploy-cpu-amd64` | 34 |
| `cu-v1-litellm-deploy-cpu-arm64` | 1 |
| `cu-v1-litellm-deploy-cpu-other` | 0 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 12 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 1 |
| `cu-v1-litellm-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cpu-amd64` | 17 |
| `cu-v1-ollama-deploy-cpu-arm64` | 0 |
| `cu-v1-ollama-deploy-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cuda-amd64` | 1 |
| `cu-v1-ollama-deploy-cuda-arm64` | 0 |
| `cu-v1-ollama-deploy-cuda-other` | 0 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 7 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 0 |
| `cu-v1-ollama-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 1 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 0 |
| `cu-v1-ollama-upgrade-cuda-other` | 0 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 24 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cpu-other` | 0 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 9 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cuda-other` | 0 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 5 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 0 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 5 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 0 |
