# Component Usage Counts

Last updated: `2026-10-16T07:11:25Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 14304 |
| deploy | 10819 |
| upgrade | 3485 |

## By Component

| Name | Count |
|---|---:|
| docling | 1127 |
| embeddings | 362 |
| kokoro | 1736 |
| litellm | 368 |
| mcp | 520 |
| ollama | 398 |
| whisper | 9178 |
| whisperlive | 615 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 11426 |
| cuda | 2878 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 10176 |
| cuda | 2878 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 12890 |
| arm64 | 1388 |
| other | 26 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 4985 |
| `cu-v1-whisper-deploy-cpu-arm64` | 868 |
| `cu-v1-whisper-deploy-cpu-other` | 1 |
| `cu-v1-whisper-deploy-cuda-amd64` | 1116 |
| `cu-v1-whisper-deploy-cuda-arm64` | 1 |
| `cu-v1-whisper-deploy-cuda-other` | 1 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 1291 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 188 |
| `cu-v1-whisper-upgrade-cpu-other` | 1 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 724 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisper-upgrade-cuda-other` | 1 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 1030 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 4 |
| `cu-v1-kokoro-deploy-cpu-other` | 1 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 335 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 1 |
| `cu-v1-kokoro-deploy-cuda-other` | 1 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 258 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 11 |
| `cu-v1-kokoro-upgrade-cpu-other` | 1 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 92 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cuda-other` | 1 |
| `cu-v1-docling-deploy-cpu-amd64` | 625 |
| `cu-v1-docling-deploy-cpu-arm64` | 154 |
| `cu-v1-docling-deploy-cpu-other` | 1 |
| `cu-v1-docling-deploy-cuda-amd64` | 121 |
| `cu-v1-docling-deploy-cuda-arm64` | 1 |
| `cu-v1-docling-deploy-cuda-other` | 1 |
| `cu-v1-docling-upgrade-cpu-amd64` | 127 |
| `cu-v1-docling-upgrade-cpu-arm64` | 14 |
| `cu-v1-docling-upgrade-cpu-other` | 1 |
| `cu-v1-docling-upgrade-cuda-amd64` | 80 |
| `cu-v1-docling-upgrade-cuda-arm64` | 1 |
| `cu-v1-docling-upgrade-cuda-other` | 1 |
| `cu-v1-mcp-deploy-cpu-amd64` | 361 |
| `cu-v1-mcp-deploy-cpu-arm64` | 35 |
| `cu-v1-mcp-deploy-cpu-other` | 1 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 108 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 14 |
| `cu-v1-mcp-upgrade-cpu-other` | 1 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 229 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 2 |
| `cu-v1-embeddings-deploy-cpu-other` | 1 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 119 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 10 |
| `cu-v1-embeddings-upgrade-cpu-other` | 1 |
| `cu-v1-litellm-deploy-cpu-amd64` | 209 |
| `cu-v1-litellm-deploy-cpu-arm64` | 31 |
| `cu-v1-litellm-deploy-cpu-other` | 1 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 116 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 10 |
| `cu-v1-litellm-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cpu-amd64` | 137 |
| `cu-v1-ollama-deploy-cpu-arm64` | 24 |
| `cu-v1-ollama-deploy-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cuda-amd64` | 87 |
| `cu-v1-ollama-deploy-cuda-arm64` | 1 |
| `cu-v1-ollama-deploy-cuda-other` | 1 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 65 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 5 |
| `cu-v1-ollama-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 74 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 1 |
| `cu-v1-ollama-upgrade-cuda-other` | 1 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 303 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 3 |
| `cu-v1-whisperlive-deploy-cpu-other` | 1 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 142 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cuda-other` | 1 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 69 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 5 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 87 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 1 |
