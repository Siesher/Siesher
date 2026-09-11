<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
  <img src="./assets/header-light.svg" width="100%" alt="Максим Сухацкий / Siesher — Data Scientist и ML Engineer. Данные, языковые модели и AI-системы. Гримуар и небесно-голубые цветы — отсылки к Фрирен.">
</picture>

<p align="center">
  <a href="https://siesher.github.io"><b>Портфолио ↗</b></a> &nbsp; · &nbsp;
  <a href="https://t.me/Siesher">Telegram</a> &nbsp; · &nbsp;
  <a href="mailto:loxterpoi@gmail.com">Email</a> &nbsp; · &nbsp;
  <a href="https://huggingface.co/Siesher">Hugging Face</a>
</p>

## Максим Сухацкий

**Data Scientist / ML Engineer · Альфа-Банк · МГТУ им. Н. Э. Баумана**

Работаю с данными в банковской сфере, исследую обучение языковых моделей и разрабатываю прикладные AI-системы. Мне интересен весь путь: постановка задачи, эксперимент, оценка качества и интеграция модели в работающий инструмент.

- **Профессиональный контекст:** банковские данные, графовая аналитика и машинное обучение.
- **Исследовательский фокус:** дообучение LLM, preference optimization и zeroth-order методы без обратного прохода.
- **Инженерная практика:** агентные пайплайны, API, локальный инференс и взаимодействие моделей с внешними системами.
- **Образование:** студент МГТУ им. Н. Э. Баумана; алгоритмы, структуры данных и C++.

<sub>Гримуар, небесно-голубые цветы и терпеливое собирание знаний — небольшие отсылки к Фрирен. Любопытство остаётся частью работы.</sub>

## Избранные проекты

<p>
  <a href="https://github.com/Siesher/MITS"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/project-mits-dark.svg"><img src="./assets/project-mits-light.svg" width="49%" alt="MITS — сократический STEM-тьютор. Мультиагентный пайплайн, символьная проверка и обучение Qwen3.5-9B."></picture></a>
  <a href="https://github.com/Siesher/dmezo"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/project-dmezo-dark.svg"><img src="./assets/project-dmezo-light.svg" width="49%" alt="D-MeZO-N — децентрализованное дообучение LLM без backpropagation. PyTorch, multi-seed эксперименты."></picture></a>
  <a href="https://github.com/Siesher/AI_For_Supreme_Com"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/project-supcom-dark.svg"><img src="./assets/project-supcom-light.svg" width="49%" alt="SupCom AI — локальный LLM-бот для Supreme Commander. C++ IPC-мост, Lua-рефлексы и fallback."></picture></a>
  <a href="https://github.com/Siesher/opencode-homelab"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/project-opencode-dark.svg"><img src="./assets/project-opencode-light.svg" width="49%" alt="OpenCode Homelab — инфраструктура локальной AI-разработки. llama.cpp, маршрутизация контекста и MCP."></picture></a>
</p>

| Проект | Технический подход | Открытые материалы |
| :--- | :--- | :--- |
| **[MITS](https://github.com/Siesher/MITS)** · исследовательский прототип | Profiler → Planner → Tutor → Verifier; граф знаний и SymPy / ChemPy. Qwen3.5-9B, GSPO → KTO → DPO; FastAPI + Next.js. | [Документация](https://github.com/Siesher/MITS/blob/main/docs/INDEX.md) · [Оценка качества](https://github.com/Siesher/MITS/blob/main/docs/diploma/phase0a_results.md) |
| **[D-MeZO-N](https://github.com/Siesher/dmezo)** · исследование | Peer-to-peer fine-tuning без backward. Адаптивное ограничение момента, drift-reset и multi-seed сравнение с vanilla MeZO. | [Математический разбор](https://github.com/Siesher/dmezo/blob/main/docs/math_intuition.md) · [Эксперименты](https://github.com/Siesher/dmezo/blob/main/docs/multiseed_analysis.md) |
| **[SupCom AI](https://github.com/Siesher/AI_For_Supreme_Com)** · прикладная система | Lua-рефлексы + Qwen3.5 4B / 9B. C++ DLL-мост, Named Pipe IPC, Python-сервер и стратегия по правилам при недоступности LLM. | [Архитектура и запуск](https://github.com/Siesher/AI_For_Supreme_Com#readme) |
| **[OpenCode Homelab](https://github.com/Siesher/opencode-homelab)** · инфраструктура | OpenCode + llama.cpp + llama-swap; выбор контекста 65K / 128K / 256K, MCP-инструменты и установочные скрипты для Windows. | [Архитектура](https://github.com/Siesher/opencode-homelab/blob/main/docs/architecture.md) · [Установка](https://github.com/Siesher/opencode-homelab/blob/main/docs/installation.md) |

## Исследования: результаты и условия

**D-MeZO-N v2.** На Qwen3.5-4B-Base / MathLogicQA средний loss снизился с **1.368 до 1.293 (−5.5%)** относительно vanilla MeZO; 3 paired seeds, одинаковое направление изменения loss во всех трёх прогонах. Прирост accuracy статистически незначим — это результат конкретного эксперимента, а не универсальное превосходство метода. [Отчёт, вариант v2 = combo](https://github.com/Siesher/dmezo/blob/main/docs/multiseed_analysis.md).

**MITS.** В production-aligned оценке на **209 STEM-задачах**: base **69.4%**, GSPO **70.3%**, KTO **69.9%**. Стек: Qwen3.5-9B, Q4_K_M, self-consistency. По предметам есть как улучшения, так и регрессии; результаты другого режима инференса рассматриваются отдельно. [Методика и разбор, 18.05.2026](https://github.com/Siesher/MITS/blob/main/docs/diploma/phase0a_results.md).

## Рабочий набор

| Направление | Инструменты и методы |
| :--- | :--- |
| **Данные и ML** | Python · SQL · Pandas · scikit-learn · Graph ML |
| **Языковые модели** | PyTorch · Transformers · LoRA · GSPO / KTO / DPO · evaluation |
| **Системы и инфраструктура** | FastAPI · llama.cpp · Ollama · MCP · Docker · Git · Linux |
| **Интеграции и интерфейсы** | C++ · Lua · TypeScript · Next.js |

## Другие эксперименты

- **[Qwen3 + LoRA](https://github.com/Siesher/Qwen3_LoRA_pet)** — адаптация языковой модели под собственные задачи.
- **[Reasoning data](https://github.com/Siesher/Generator_for_reasoning)** — генерация данных для обучения рассуждению.
- **[Speech recognition](https://github.com/Siesher/Whisper_or_no_Whisper)** — эксперименты с Whisper, Wav2Vec и Silero.
- **[C++ / BMSTU](https://github.com/Siesher/BMSTU-CPP-Labs)** — алгоритмы и структуры данных в учебных работах.

## Open-source практика

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Siesher/Siesher/output/github-snake-dark.svg">
  <img src="https://raw.githubusercontent.com/Siesher/Siesher/output/github-snake.svg" width="100%" alt="Анимированная карта вкладов в GitHub.">
</picture>

<details>
<summary>Трёхмерная карта вкладов</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-view.svg">
  <img src="./profile-3d-contrib/profile-season.svg" width="100%" alt="Трёхмерная карта вкладов GitHub.">
</picture>

</details>

---

**Для связи:** [Telegram](https://t.me/Siesher) · [loxterpoi@gmail.com](mailto:loxterpoi@gmail.com)<br>
LLM-исследования, прикладное машинное обучение и AI-инструменты. [Подробнее обо мне и проектах →](https://siesher.github.io)

<sub>✦ Ещё одна задача. Ещё одно открытие по пути.</sub>
