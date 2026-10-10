# Component Usage Counts

Last updated: `2026-10-10T08:30:39Z`

Counts are approximate GitHub release asset download counts, not unique users or active installs.
The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.
The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.

## Totals

| Metric | Count |
|---|---:|
| all | 13324 |
| deploy | 10099 |
| upgrade | 3225 |

## By Component

| Name | Count |
|---|---:|
| docling | 1024 |
| embeddings | 333 |
| kokoro | 1582 |
| litellm | 350 |
| mcp | 482 |
| ollama | 385 |
| whisper | 8601 |
| whisperlive | 567 |

## By Image Variant

| Name | Count |
|---|---:|
| cpu | 10646 |
| cuda | 2678 |

## By Image Variant (CUDA-Capable Components Only)

| Name | Count |
|---|---:|
| cpu | 9481 |
| cuda | 2678 |

## By Architecture

| Name | Count |
|---|---:|
| amd64 | 12024 |
| arm64 | 1274 |
| other | 26 |

## Raw Counters

| Asset | Count |
|---|---:|
| `cu-v1-whisper-deploy-cpu-amd64` | 4709 |
| `cu-v1-whisper-deploy-cpu-arm64` | 809 |
| `cu-v1-whisper-deploy-cpu-other` | 1 |
| `cu-v1-whisper-deploy-cuda-amd64` | 1039 |
| `cu-v1-whisper-deploy-cuda-arm64` | 1 |
| `cu-v1-whisper-deploy-cuda-other` | 1 |
| `cu-v1-whisper-upgrade-cpu-amd64` | 1193 |
| `cu-v1-whisper-upgrade-cpu-arm64` | 175 |
| `cu-v1-whisper-upgrade-cpu-other` | 1 |
| `cu-v1-whisper-upgrade-cuda-amd64` | 670 |
| `cu-v1-whisper-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisper-upgrade-cuda-other` | 1 |
| `cu-v1-kokoro-deploy-cpu-amd64` | 931 |
| `cu-v1-kokoro-deploy-cpu-arm64` | 4 |
| `cu-v1-kokoro-deploy-cpu-other` | 1 |
| `cu-v1-kokoro-deploy-cuda-amd64` | 311 |
| `cu-v1-kokoro-deploy-cuda-arm64` | 1 |
| `cu-v1-kokoro-deploy-cuda-other` | 1 |
| `cu-v1-kokoro-upgrade-cpu-amd64` | 234 |
| `cu-v1-kokoro-upgrade-cpu-arm64` | 10 |
| `cu-v1-kokoro-upgrade-cpu-other` | 1 |
| `cu-v1-kokoro-upgrade-cuda-amd64` | 86 |
| `cu-v1-kokoro-upgrade-cuda-arm64` | 1 |
| `cu-v1-kokoro-upgrade-cuda-other` | 1 |
| `cu-v1-docling-deploy-cpu-amd64` | 584 |
| `cu-v1-docling-deploy-cpu-arm64` | 116 |
| `cu-v1-docling-deploy-cpu-other` | 1 |
| `cu-v1-docling-deploy-cuda-amd64` | 109 |
| `cu-v1-docling-deploy-cuda-arm64` | 1 |
| `cu-v1-docling-deploy-cuda-other` | 1 |
| `cu-v1-docling-upgrade-cpu-amd64` | 119 |
| `cu-v1-docling-upgrade-cpu-arm64` | 13 |
| `cu-v1-docling-upgrade-cpu-other` | 1 |
| `cu-v1-docling-upgrade-cuda-amd64` | 77 |
| `cu-v1-docling-upgrade-cuda-arm64` | 1 |
| `cu-v1-docling-upgrade-cuda-other` | 1 |
| `cu-v1-mcp-deploy-cpu-amd64` | 337 |
| `cu-v1-mcp-deploy-cpu-arm64` | 35 |
| `cu-v1-mcp-deploy-cpu-other` | 1 |
| `cu-v1-mcp-upgrade-cpu-amd64` | 96 |
| `cu-v1-mcp-upgrade-cpu-arm64` | 12 |
| `cu-v1-mcp-upgrade-cpu-other` | 1 |
| `cu-v1-embeddings-deploy-cpu-amd64` | 213 |
| `cu-v1-embeddings-deploy-cpu-arm64` | 2 |
| `cu-v1-embeddings-deploy-cpu-other` | 1 |
| `cu-v1-embeddings-upgrade-cpu-amd64` | 106 |
| `cu-v1-embeddings-upgrade-cpu-arm64` | 10 |
| `cu-v1-embeddings-upgrade-cpu-other` | 1 |
| `cu-v1-litellm-deploy-cpu-amd64` | 198 |
| `cu-v1-litellm-deploy-cpu-arm64` | 31 |
| `cu-v1-litellm-deploy-cpu-other` | 1 |
| `cu-v1-litellm-upgrade-cpu-amd64` | 109 |
| `cu-v1-litellm-upgrade-cpu-arm64` | 10 |
| `cu-v1-litellm-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cpu-amd64` | 133 |
| `cu-v1-ollama-deploy-cpu-arm64` | 24 |
| `cu-v1-ollama-deploy-cpu-other` | 1 |
| `cu-v1-ollama-deploy-cuda-amd64` | 83 |
| `cu-v1-ollama-deploy-cuda-arm64` | 1 |
| `cu-v1-ollama-deploy-cuda-other` | 1 |
| `cu-v1-ollama-upgrade-cpu-amd64` | 63 |
| `cu-v1-ollama-upgrade-cpu-arm64` | 5 |
| `cu-v1-ollama-upgrade-cpu-other` | 1 |
| `cu-v1-ollama-upgrade-cuda-amd64` | 71 |
| `cu-v1-ollama-upgrade-cuda-arm64` | 1 |
| `cu-v1-ollama-upgrade-cuda-other` | 1 |
| `cu-v1-whisperlive-deploy-cpu-amd64` | 278 |
| `cu-v1-whisperlive-deploy-cpu-arm64` | 3 |
| `cu-v1-whisperlive-deploy-cpu-other` | 1 |
| `cu-v1-whisperlive-deploy-cuda-amd64` | 132 |
| `cu-v1-whisperlive-deploy-cuda-arm64` | 1 |
| `cu-v1-whisperlive-deploy-cuda-other` | 1 |
| `cu-v1-whisperlive-upgrade-cpu-amd64` | 63 |
| `cu-v1-whisperlive-upgrade-cpu-arm64` | 5 |
| `cu-v1-whisperlive-upgrade-cpu-other` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-amd64` | 80 |
| `cu-v1-whisperlive-upgrade-cuda-arm64` | 1 |
| `cu-v1-whisperlive-upgrade-cuda-other` | 1 |
