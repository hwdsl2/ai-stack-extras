# Component Usage Counts

Last updated: `2026-07-29T10:48:27Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 3735 |
| deploy | 2861 |
| upgrade | 874 |

## By Component

| Name | Count |
|---|---:|
| docling | 251 |
| embeddings | 117 |
| kokoro | 470 |
| litellm | 192 |
| mcp | 184 |
| ollama | 108 |
| whisper | 2242 |
| whisperlive | 171 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 2898 |
| cuda | 837 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 2405 |
| cuda | 837 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 3379 |
| arm64 | 356 |
| other | 0 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 1146 |
| `cu-v1-whisper-deploy-cpu-arm64` | 199 |
| `cu-v1-whisper-deploy-cpu-other` | 0 |
| `cu-v1-whisper-deploy-cuda-amd64` | 400 |
| `cu-v1-whisper-deploy-cuda-arm64` | 0 |
| `cu-v1-whisper-deploy-cuda-other` | 0 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 249 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 36 |
| `cu-v1-whisper-upgrade-cpu-other` | 0 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 212 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisper-upgrade-cuda-other` | 0 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 299 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 1 |
| `cu-v1-kokoro-deploy-cpu-other` | 0 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 68 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 0 |
| `cu-v1-kokoro-deploy-cuda-other` | 0 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 78 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 4 |
| `cu-v1-kokoro-upgrade-cpu-other` | 0 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 20 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 0 |
| `cu-v1-kokoro-upgrade-cuda-other` | 0 |
| `cu-v1-docling-deploy-cpu-amd64` | 163 |
| `cu-v1-docling-deploy-cpu-arm64` | 24 |
| `cu-v1-docling-deploy-cpu-other` | 0 |
| `cu-v1-docling-deploy-cuda-amd64` | 30 |
| `cu-v1-docling-deploy-cuda-arm64` | 0 |
| `cu-v1-docling-deploy-cuda-other` | 0 |
| `cu-v1-docling-upgrade-cpu-amd64` | 25 |
| `cu-v1-docling-upgrade-cpu-arm64` | 1 |
| `cu-v1-docling-upgrade-cpu-other` | 0 |
| `cu-v1-docling-upgrade-cuda-amd64` | 8 |
| `cu-v1-docling-upgrade-cuda-arm64` | 0 |
| `cu-v1-docling-upgrade-cuda-other` | 0 |
| `cu-v1-mcp-deploy-cpu-amd64` | 101 |
| `cu-v1-mcp-deploy-cpu-arm64` | 22 |
| `cu-v1-mcp-deploy-cpu-other` | 0 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 54 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 7 |
| `cu-v1-mcp-upgrade-cpu-other` | 0 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 75 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 9 |
| `cu-v1-embeddings-deploy-cpu-other` | 0 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 33 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 0 |
| `cu-v1-embeddings-upgrade-cpu-other` | 0 |
| `cu-v1-litellm-deploy-cpu-amd64` | 102 |
| `cu-v1-litellm-deploy-cpu-arm64` | 15 |
| `cu-v1-litellm-deploy-cpu-other` | 0 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 51 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 24 |
| `cu-v1-litellm-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cpu-amd64` | 66 |
| `cu-v1-ollama-deploy-cpu-arm64` | 8 |
| `cu-v1-ollama-deploy-cpu-other` | 0 |
| `cu-v1-ollama-deploy-cuda-amd64` | 6 |
| `cu-v1-ollama-deploy-cuda-arm64` | 0 |
| `cu-v1-ollama-deploy-cuda-other` | 0 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 11 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 2 |
| `cu-v1-ollama-upgrade-cpu-other` | 0 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 15 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 0 |
| `cu-v1-ollama-upgrade-cuda-other` | 0 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 71 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cpu-other` | 0 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 55 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 0 |
| `cu-v1-whisperlive-deploy-cuda-other` | 0 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 18 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 3 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 23 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 0 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 0 |
