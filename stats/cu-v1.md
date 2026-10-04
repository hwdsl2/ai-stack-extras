# Component Usage Counts

Last updated: `2026-10-04T08:27:50Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 12005 |
| deploy | 9240 |
| upgrade | 2765 |

## By Component

| Name | Count |
|---|---:|
| docling | 945 |
| embeddings | 284 |
| kokoro | 1432 |
| litellm | 320 |
| mcp | 453 |
| ollama | 360 |
| whisper | 7688 |
| whisperlive | 523 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 9565 |
| cuda | 2440 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 8508 |
| cuda | 2440 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 10835 |
| arm64 | 1144 |
| other | 26 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 4268 |
| `cu-v1-whisper-deploy-cpu-arm64` | 703 |
| `cu-v1-whisper-deploy-cpu-other` | 1 |
| `cu-v1-whisper-deploy-cuda-amd64` | 982 |
| `cu-v1-whisper-deploy-cuda-arm64` | 1 |
| `cu-v1-whisper-deploy-cuda-other` | 1 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 1004 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 157 |
| `cu-v1-whisper-upgrade-cpu-other` | 1 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 568 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisper-upgrade-cuda-other` | 1 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 849 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 4 |
| `cu-v1-kokoro-deploy-cpu-other` | 1 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 288 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 1 |
| `cu-v1-kokoro-deploy-cuda-other` | 1 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 203 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 9 |
| `cu-v1-kokoro-upgrade-cpu-other` | 1 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 73 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cuda-other` | 1 |
| `cu-v1-docling-deploy-cpu-amd64` | 539 |
| `cu-v1-docling-deploy-cpu-arm64` | 114 |
| `cu-v1-docling-deploy-cpu-other` | 1 |
| `cu-v1-docling-deploy-cuda-amd64` | 100 |
| `cu-v1-docling-deploy-cuda-arm64` | 1 |
| `cu-v1-docling-deploy-cuda-other` | 1 |
| `cu-v1-docling-upgrade-cpu-amd64` | 101 |
| `cu-v1-docling-upgrade-cpu-arm64` | 11 |
| `cu-v1-docling-upgrade-cpu-other` | 1 |
| `cu-v1-docling-upgrade-cuda-amd64` | 74 |
| `cu-v1-docling-upgrade-cuda-arm64` | 1 |
| `cu-v1-docling-upgrade-cuda-other` | 1 |
| `cu-v1-mcp-deploy-cpu-amd64` | 318 |
| `cu-v1-mcp-deploy-cpu-arm64` | 35 |
| `cu-v1-mcp-deploy-cpu-other` | 1 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 86 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 12 |
| `cu-v1-mcp-upgrade-cpu-other` | 1 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 191 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 2 |
| `cu-v1-embeddings-deploy-cpu-other` | 1 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 79 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 10 |
| `cu-v1-embeddings-upgrade-cpu-other` | 1 |
| `cu-v1-litellm-deploy-cpu-amd64` | 182 |
| `cu-v1-litellm-deploy-cpu-arm64` | 30 |
| `cu-v1-litellm-deploy-cpu-other` | 1 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 96 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 10 |
| `cu-v1-litellm-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cpu-amd64` | 124 |
| `cu-v1-ollama-deploy-cpu-arm64` | 24 |
| `cu-v1-ollama-deploy-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cuda-amd64` | 82 |
| `cu-v1-ollama-deploy-cuda-arm64` | 1 |
| `cu-v1-ollama-deploy-cuda-other` | 1 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 55 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 5 |
| `cu-v1-ollama-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 64 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 1 |
| `cu-v1-ollama-upgrade-cuda-other` | 1 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 263 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 3 |
| `cu-v1-whisperlive-deploy-cpu-other` | 1 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 121 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cuda-other` | 1 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 57 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 5 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 68 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 1 |
