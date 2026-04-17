# The Founder's Errata

An *errata* is a formal notice of correction attached to a previously published work, so that the original and the correction are read together. This repository applies the convention to the judgments of a single founder, Dr. Jee Hoon Ju, concerning AetherHeal Co., Ltd. and adjacent work. Each entry records a specific reversal — a position once held, a position now held, and the cause of the change — and accumulates as an append-only public record over time.

## Schema

Every entry contains three fields. An entry missing any of these is invalid.

- **Prior Position** — what was previously held.
- **Current Position** — what is now held.
- **Causal Update** — the specific evidence, argument, or experience that caused the change.

## Append-only

Entries are never deleted or rewritten. If a past entry is later judged to be itself in error, a new entry is written that reverses it; the original remains visible. The authoritative timestamp of each entry is its git commit timestamp.

## Disclaimer

This is a personal record maintained by the founder. It is not an official communication of AetherHeal Co., Ltd.

## Entries

See the [entries directory](entries/) for the full list. The published site lists all entries in reverse chronological order.

## Deployment

Published at `https://jeehoonju.com/errata/`. The site is served by GitHub Pages as a project site under the user `dr-jeehoonju`. The custom domain `jeehoonju.com` is configured on the companion repository `dr-jeehoonju/dr-jeehoonju.github.io`; this repository inherits the apex domain and is served under the path `/errata/`. The Eleventy build writes static HTML into `docs/`, which is committed to the `main` branch. GitHub Pages is configured to serve the site from `main` branch, `/docs` folder.

The build is intentionally local-only. There is no GitHub Actions workflow. Validation runs by invoking `python3 scripts/validate.py` (zero external dependencies beyond the Python 3 standard library) before each commit. This choice is deliberate: the project's design horizon is a decade or more, and a local toolchain of plain Markdown, plain git, and a small Eleventy build has a longer expected lifetime than any hosted CI dependency.

### Authoring a new entry

```
./scripts/new-entry.sh          # prompts for slug, creates the file, opens $EDITOR
python3 scripts/validate.py     # runs the three-field and filename checks
npx eleventy                    # rebuilds docs/
git add -A && git commit -m "..." && git push
```

### First-time setup on a fresh clone

```
npm install                     # installs Eleventy
npx eleventy                    # builds docs/
```

### One-time GitHub Pages configuration

After the first push creates the `main` branch, run once:

```
gh api -X POST /repos/dr-jeehoonju/errata/pages \
  -f 'source[branch]=main' -f 'source[path]=/docs'
```

Or in the web UI: `Settings` → `Pages` → Source: `main`, `/docs`. No custom-domain field is needed here; the domain is inherited from the user-site repository.

---

## 창업자 정오표 (한국어)

*정오표(errata)*는 이미 출판된 저작물에 첨부되는 공식적인 정정 기록으로, 원본과 정정이 함께 읽히도록 보존됩니다. 본 저장소는 이 관행을 한 창업자, 주지훈(Dr. Jee Hoon Ju)의 AetherHeal Co., Ltd. 및 관련 활동에 관한 판단에 적용합니다. 각 항목은 구체적인 판단의 번복 — 이전에 지녔던 입장, 현재 지니는 입장, 그리고 변화의 원인 — 을 기록하며, 시간이 지남에 따라 추가만 가능한(append-only) 공개 기록으로 축적됩니다.

### 스키마

모든 항목은 다음 세 가지 필드를 포함합니다. 하나라도 누락된 항목은 유효하지 않습니다.

- **이전 입장 (Prior Position)** — 이전에 지녔던 입장.
- **현재 입장 (Current Position)** — 현재 지니는 입장.
- **인과적 갱신 (Causal Update)** — 판단의 변화를 초래한 구체적인 증거, 논거, 또는 경험.

### 추가 전용 (Append-only)

항목은 삭제되거나 재작성되지 않습니다. 과거 항목이 이후에 잘못되었다고 판단될 경우, 이를 번복하는 새로운 항목이 추가되며, 원본은 그대로 남습니다. 각 항목의 공식 타임스탬프는 git 커밋 타임스탬프입니다.

### 고지

본 저장소는 창업자 개인이 관리하는 기록이며, AetherHeal Co., Ltd.의 공식 커뮤니케이션이 아닙니다.
