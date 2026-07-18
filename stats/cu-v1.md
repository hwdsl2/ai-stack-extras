# Component Usage Counts

Last updated: `2026-07-18T15:14:26Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 1755 |
| deploy | 1237 |
| upgrade | 518 |

## By Component

| Name | Count |
|---|---:|
| docling | 127 |
| embeddings | 43 |
| kokoro | 221 |
| litellm | 104 |
| mcp | 72 |
| ollama | 55 |
| whisper | 1045 |
| whisperlive | 88 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 1365 |
| cuda | 390 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 1146 |
| cuda | 390 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 1600 |
| arm64 | 155 |
| other | 0 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 471 |
| `cu-v1-whisper-deploy-cpu-arm64` | 85 |
| `cu-v1-whisper-deploy-cpu-other` | 0 |
| `cu-v1-whisper-deploy-cuda-amd64` | 170 |
| `cu-v1-whisper-deploy-cuda-arm64` | 0 |
| `cu-v1-whisper-deploy-cuda-other` | 0 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 167 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 21 |
| `cu-v1-whisper-upgrade-cpu-other` | 0 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 131 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisper-upgrade-cuda-other` | 0 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 142 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 0 |
| `cu-v1-kokoro-deploy-cpu-other` | 0 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 23 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 0 |
| `cu-v1-kokoro-deploy-cuda-other` | 0 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 45 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cpu-other` | 0 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 10 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 0 |
| `cu-v1-kokoro-upgrade-cuda-other` | 0 |
| `cu-v1-docling-deploy-cpu-amd64` | 85 |
| `cu-v1-docling-deploy-cpu-arm64` | 12 |
| `cu-v1-docling-deploy-cpu-other` | 0 |
| `cu-v1-docling-deploy-cuda-amd64` | 15 |
| `cu-v1-docling-deploy-cuda-arm64` | 0 |
| `cu-v1-docling-deploy-cuda-other` | 0 |
| `cu-v1-docling-upgrade-cpu-amd64` | 12 |
| `cu-v1-docling-upgrade-cpu-arm64` | 0 |
| `cu-v1-docling-upgrade-cpu-other` | 0 |
| `cu-v1-docling-upgrade-cuda-amd64` | 3 |
| `cu-v1-docling-upgrade-cuda-arm64` | 0 |
| `cu-v1-docling-upgrade-cuda-other` | 0 |
| `cu-v1-mcp-deploy-cpu-amd64` | 42 |
| `cu-v1-mcp-deploy-cpu-arm64` | 1 |
| `cu-v1-mcp-deploy-cpu-other` | 0 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 23 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 6 |
| `cu-v1-mcp-upgrade-cpu-other` | 0 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 25 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 3 |
| `cu-v1-embeddings-deploy-cpu-other` | 0 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 15 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 0 |
| `cu-v1-embeddings-upgrade-cpu-other` | 0 |
| `cu-v1-litellm-deploy-cpu-amd64` | 56 |
| `cu-v1-litellm-deploy-cpu-arm64` | 6 |
| `cu-v1-litellm-deploy-cpu-other` | 0 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 29 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 13 |
| `cu-v1-litellm-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cpu-amd64` | 35 |
| `cu-v1-ollama-deploy-cpu-arm64` | 3 |
| `cu-v1-ollama-deploy-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cuda-amd64` | 2 |
| `cu-v1-ollama-deploy-cuda-arm64` | 0 |
| `cu-v1-ollama-deploy-cuda-other` | 0 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 8 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 1 |
| `cu-v1-ollama-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 6 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 0 |
| `cu-v1-ollama-upgrade-cuda-other` | 0 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 43 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cpu-other` | 0 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 17 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cuda-other` | 0 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 12 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 2 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 13 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 0 |
