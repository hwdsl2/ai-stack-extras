# Component Usage Counts

Last updated: `2026-11-26T10:55:28Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 20796 |
| deploy | 15151 |
| upgrade | 5645 |

## By Component

| Name | Count |
|---|---:|
| docling | 1693 |
| embeddings | 608 |
| kokoro | 2712 |
| litellm | 553 |
| mcp | 733 |
| ollama | 602 |
| whisper | 13042 |
| whisperlive | 853 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 16678 |
| cuda | 4118 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 14784 |
| cuda | 4118 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 18731 |
| arm64 | 2013 |
| other | 52 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 6723 |
| `cu-v1-whisper-deploy-cpu-arm64` | 1175 |
| `cu-v1-whisper-deploy-cpu-other` | 2 |
| `cu-v1-whisper-deploy-cuda-amd64` | 1482 |
| `cu-v1-whisper-deploy-cuda-arm64` | 2 |
| `cu-v1-whisper-deploy-cuda-other` | 2 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 2215 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 282 |
| `cu-v1-whisper-upgrade-cpu-other` | 2 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 1153 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisper-upgrade-cuda-other` | 2 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 1611 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 36 |
| `cu-v1-kokoro-deploy-cpu-other` | 2 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 439 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 2 |
| `cu-v1-kokoro-deploy-cuda-other` | 2 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 432 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 20 |
| `cu-v1-kokoro-upgrade-cpu-other` | 2 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 162 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 2 |
| `cu-v1-kokoro-upgrade-cuda-other` | 2 |
| `cu-v1-docling-deploy-cpu-amd64` | 973 |
| `cu-v1-docling-deploy-cpu-arm64` | 180 |
| `cu-v1-docling-deploy-cpu-other` | 2 |
| `cu-v1-docling-deploy-cuda-amd64` | 201 |
| `cu-v1-docling-deploy-cuda-arm64` | 2 |
| `cu-v1-docling-deploy-cuda-other` | 2 |
| `cu-v1-docling-upgrade-cpu-amd64` | 207 |
| `cu-v1-docling-upgrade-cpu-arm64` | 23 |
| `cu-v1-docling-upgrade-cpu-other` | 2 |
| `cu-v1-docling-upgrade-cuda-amd64` | 97 |
| `cu-v1-docling-upgrade-cuda-arm64` | 2 |
| `cu-v1-docling-upgrade-cuda-other` | 2 |
| `cu-v1-mcp-deploy-cpu-amd64` | 497 |
| `cu-v1-mcp-deploy-cpu-arm64` | 46 |
| `cu-v1-mcp-deploy-cpu-other` | 2 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 170 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 16 |
| `cu-v1-mcp-upgrade-cpu-other` | 2 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 330 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 76 |
| `cu-v1-embeddings-deploy-cpu-other` | 2 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 180 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 18 |
| `cu-v1-embeddings-upgrade-cpu-other` | 2 |
| `cu-v1-litellm-deploy-cpu-amd64` | 327 |
| `cu-v1-litellm-deploy-cpu-arm64` | 51 |
| `cu-v1-litellm-deploy-cpu-other` | 2 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 155 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 16 |
| `cu-v1-litellm-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cpu-amd64` | 225 |
| `cu-v1-ollama-deploy-cpu-arm64` | 30 |
| `cu-v1-ollama-deploy-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cuda-amd64` | 121 |
| `cu-v1-ollama-deploy-cuda-arm64` | 2 |
| `cu-v1-ollama-deploy-cuda-other` | 2 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 99 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 7 |
| `cu-v1-ollama-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 108 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 2 |
| `cu-v1-ollama-upgrade-cuda-other` | 2 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 406 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 8 |
| `cu-v1-whisperlive-deploy-cpu-other` | 2 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 178 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 2 |
| `cu-v1-whisperlive-deploy-cuda-other` | 2 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 103 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 9 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 137 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 2 |
