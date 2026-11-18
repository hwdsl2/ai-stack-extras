# Component Usage Counts

Last updated: `2026-11-18T10:11:34Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 20037 |
| deploy | 14613 |
| upgrade | 5424 |

## By Component

| Name | Count |
|---|---:|
| docling | 1612 |
| embeddings | 594 |
| kokoro | 2631 |
| litellm | 542 |
| mcp | 714 |
| ollama | 591 |
| whisper | 12542 |
| whisperlive | 811 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 16064 |
| cuda | 3973 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 14214 |
| cuda | 3973 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 18047 |
| arm64 | 1938 |
| other | 52 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 6484 |
| `cu-v1-whisper-deploy-cpu-arm64` | 1125 |
| `cu-v1-whisper-deploy-cpu-other` | 2 |
| `cu-v1-whisper-deploy-cuda-amd64` | 1413 |
| `cu-v1-whisper-deploy-cuda-arm64` | 2 |
| `cu-v1-whisper-deploy-cuda-other` | 2 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 2124 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 271 |
| `cu-v1-whisper-upgrade-cpu-other` | 2 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 1113 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisper-upgrade-cuda-other` | 2 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 1564 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 32 |
| `cu-v1-kokoro-deploy-cpu-other` | 2 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 435 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 2 |
| `cu-v1-kokoro-deploy-cuda-other` | 2 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 414 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 20 |
| `cu-v1-kokoro-upgrade-cpu-other` | 2 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 154 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 2 |
| `cu-v1-kokoro-upgrade-cuda-other` | 2 |
| `cu-v1-docling-deploy-cpu-amd64` | 915 |
| `cu-v1-docling-deploy-cpu-arm64` | 174 |
| `cu-v1-docling-deploy-cpu-other` | 2 |
| `cu-v1-docling-deploy-cuda-amd64` | 198 |
| `cu-v1-docling-deploy-cuda-arm64` | 2 |
| `cu-v1-docling-deploy-cuda-other` | 2 |
| `cu-v1-docling-upgrade-cpu-amd64` | 196 |
| `cu-v1-docling-upgrade-cpu-arm64` | 23 |
| `cu-v1-docling-upgrade-cpu-other` | 2 |
| `cu-v1-docling-upgrade-cuda-amd64` | 94 |
| `cu-v1-docling-upgrade-cuda-arm64` | 2 |
| `cu-v1-docling-upgrade-cuda-other` | 2 |
| `cu-v1-mcp-deploy-cpu-amd64` | 486 |
| `cu-v1-mcp-deploy-cpu-arm64` | 46 |
| `cu-v1-mcp-deploy-cpu-other` | 2 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 162 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 16 |
| `cu-v1-mcp-upgrade-cpu-other` | 2 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 325 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 76 |
| `cu-v1-embeddings-deploy-cpu-other` | 2 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 171 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 18 |
| `cu-v1-embeddings-upgrade-cpu-other` | 2 |
| `cu-v1-litellm-deploy-cpu-amd64` | 323 |
| `cu-v1-litellm-deploy-cpu-arm64` | 51 |
| `cu-v1-litellm-deploy-cpu-other` | 2 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 149 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 15 |
| `cu-v1-litellm-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cpu-amd64` | 221 |
| `cu-v1-ollama-deploy-cpu-arm64` | 30 |
| `cu-v1-ollama-deploy-cpu-other` | 2 |
| `cu-v1-ollama-deploy-cuda-amd64` | 120 |
| `cu-v1-ollama-deploy-cuda-arm64` | 2 |
| `cu-v1-ollama-deploy-cuda-other` | 2 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 98 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 7 |
| `cu-v1-ollama-upgrade-cpu-other` | 2 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 103 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 2 |
| `cu-v1-ollama-upgrade-cuda-other` | 2 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 384 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 6 |
| `cu-v1-whisperlive-deploy-cpu-other` | 2 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 169 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 2 |
| `cu-v1-whisperlive-deploy-cuda-other` | 2 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 98 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 8 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 134 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 2 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 2 |
