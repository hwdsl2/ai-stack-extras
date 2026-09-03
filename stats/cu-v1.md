# Component Usage Counts

Last updated: `2026-09-03T07:11:17Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 6258 |
| deploy | 5000 |
| upgrade | 1258 |

## By Component

| Name | Count |
|---|---:|
| docling | 449 |
| embeddings | 145 |
| kokoro | 563 |
| litellm | 203 |
| mcp | 254 |
| ollama | 228 |
| whisper | 4193 |
| whisperlive | 223 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 5063 |
| cuda | 1195 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 4461 |
| cuda | 1195 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 5551 |
| arm64 | 707 |
| other | 0 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 2396 |
| `cu-v1-whisper-deploy-cpu-arm64` | 456 |
| `cu-v1-whisper-deploy-cpu-other` | 0 |
| `cu-v1-whisper-deploy-cuda-amd64` | 540 |
| `cu-v1-whisper-deploy-cuda-arm64` | 0 |
| `cu-v1-whisper-deploy-cuda-other` | 0 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 459 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 75 |
| `cu-v1-whisper-upgrade-cpu-other` | 0 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 267 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisper-upgrade-cuda-other` | 0 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 314 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 0 |
| `cu-v1-kokoro-deploy-cpu-other` | 0 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 130 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 0 |
| `cu-v1-kokoro-deploy-cuda-other` | 0 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 86 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 4 |
| `cu-v1-kokoro-upgrade-cpu-other` | 0 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 29 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 0 |
| `cu-v1-kokoro-upgrade-cuda-other` | 0 |
| `cu-v1-docling-deploy-cpu-amd64` | 264 |
| `cu-v1-docling-deploy-cpu-arm64` | 84 |
| `cu-v1-docling-deploy-cpu-other` | 0 |
| `cu-v1-docling-deploy-cuda-amd64` | 49 |
| `cu-v1-docling-deploy-cuda-arm64` | 0 |
| `cu-v1-docling-deploy-cuda-other` | 0 |
| `cu-v1-docling-upgrade-cpu-amd64` | 36 |
| `cu-v1-docling-upgrade-cpu-arm64` | 7 |
| `cu-v1-docling-upgrade-cpu-other` | 0 |
| `cu-v1-docling-upgrade-cuda-amd64` | 9 |
| `cu-v1-docling-upgrade-cuda-arm64` | 0 |
| `cu-v1-docling-upgrade-cuda-other` | 0 |
| `cu-v1-mcp-deploy-cpu-amd64` | 174 |
| `cu-v1-mcp-deploy-cpu-arm64` | 26 |
| `cu-v1-mcp-deploy-cpu-other` | 0 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 51 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 3 |
| `cu-v1-mcp-upgrade-cpu-other` | 0 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 108 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 0 |
| `cu-v1-embeddings-deploy-cpu-other` | 0 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 31 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 6 |
| `cu-v1-embeddings-upgrade-cpu-other` | 0 |
| `cu-v1-litellm-deploy-cpu-amd64` | 118 |
| `cu-v1-litellm-deploy-cpu-arm64` | 18 |
| `cu-v1-litellm-deploy-cpu-other` | 0 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 64 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 3 |
| `cu-v1-litellm-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cpu-amd64` | 87 |
| `cu-v1-ollama-deploy-cpu-arm64` | 20 |
| `cu-v1-ollama-deploy-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cuda-amd64` | 34 |
| `cu-v1-ollama-deploy-cuda-arm64` | 0 |
| `cu-v1-ollama-deploy-cuda-other` | 0 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 30 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 4 |
| `cu-v1-ollama-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 53 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 0 |
| `cu-v1-ollama-upgrade-cuda-other` | 0 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 122 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cpu-other` | 0 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 60 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cuda-other` | 0 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 16 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 1 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 24 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 0 |
