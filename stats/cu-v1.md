# Component Usage Counts

Last updated: `2026-10-05T09:06:19Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 12242 |
| deploy | 9403 |
| upgrade | 2839 |

## By Component

| Name | Count |
|---|---:|
| docling | 959 |
| embeddings | 289 |
| kokoro | 1465 |
| litellm | 324 |
| mcp | 455 |
| ollama | 362 |
| whisper | 7855 |
| whisperlive | 533 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 9750 |
| cuda | 2492 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 8682 |
| cuda | 2492 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 11056 |
| arm64 | 1160 |
| other | 26 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 4364 |
| `cu-v1-whisper-deploy-cpu-arm64` | 713 |
| `cu-v1-whisper-deploy-cpu-other` | 1 |
| `cu-v1-whisper-deploy-cuda-amd64` | 990 |
| `cu-v1-whisper-deploy-cuda-arm64` | 1 |
| `cu-v1-whisper-deploy-cuda-other` | 1 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 1031 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 161 |
| `cu-v1-whisper-upgrade-cpu-other` | 1 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 590 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisper-upgrade-cuda-other` | 1 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 867 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 4 |
| `cu-v1-kokoro-deploy-cpu-other` | 1 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 294 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 1 |
| `cu-v1-kokoro-deploy-cuda-other` | 1 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 208 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 9 |
| `cu-v1-kokoro-upgrade-cpu-other` | 1 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 77 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cuda-other` | 1 |
| `cu-v1-docling-deploy-cpu-amd64` | 544 |
| `cu-v1-docling-deploy-cpu-arm64` | 114 |
| `cu-v1-docling-deploy-cpu-other` | 1 |
| `cu-v1-docling-deploy-cuda-amd64` | 104 |
| `cu-v1-docling-deploy-cuda-arm64` | 1 |
| `cu-v1-docling-deploy-cuda-other` | 1 |
| `cu-v1-docling-upgrade-cpu-amd64` | 105 |
| `cu-v1-docling-upgrade-cpu-arm64` | 12 |
| `cu-v1-docling-upgrade-cpu-other` | 1 |
| `cu-v1-docling-upgrade-cuda-amd64` | 74 |
| `cu-v1-docling-upgrade-cuda-arm64` | 1 |
| `cu-v1-docling-upgrade-cuda-other` | 1 |
| `cu-v1-mcp-deploy-cpu-amd64` | 320 |
| `cu-v1-mcp-deploy-cpu-arm64` | 35 |
| `cu-v1-mcp-deploy-cpu-other` | 1 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 86 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 12 |
| `cu-v1-mcp-upgrade-cpu-other` | 1 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 193 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 2 |
| `cu-v1-embeddings-deploy-cpu-other` | 1 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 82 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 10 |
| `cu-v1-embeddings-upgrade-cpu-other` | 1 |
| `cu-v1-litellm-deploy-cpu-amd64` | 185 |
| `cu-v1-litellm-deploy-cpu-arm64` | 31 |
| `cu-v1-litellm-deploy-cpu-other` | 1 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 96 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 10 |
| `cu-v1-litellm-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cpu-amd64` | 125 |
| `cu-v1-ollama-deploy-cpu-arm64` | 24 |
| `cu-v1-ollama-deploy-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cuda-amd64` | 83 |
| `cu-v1-ollama-deploy-cuda-arm64` | 1 |
| `cu-v1-ollama-deploy-cuda-other` | 1 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 55 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 5 |
| `cu-v1-ollama-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 64 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 1 |
| `cu-v1-ollama-upgrade-cuda-other` | 1 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 265 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 3 |
| `cu-v1-whisperlive-deploy-cpu-other` | 1 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 125 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cuda-other` | 1 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 58 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 5 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 71 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 1 |
