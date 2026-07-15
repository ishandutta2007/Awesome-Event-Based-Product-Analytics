import os
import re
import subprocess

REPO_DIR = r"C:\Users\ishan\Documents\Projects\Awesome-Event-Based-Product-Analytics"
README_PATH = os.path.join(REPO_DIR, "README.md")

def run_git(commit_msg):
    # Add changes
    subprocess.run(["git", "-C", REPO_DIR, "add", "."], check=True)
    # Commit changes
    try:
        subprocess.run(["git", "-C", REPO_DIR, "commit", "-m", commit_msg], check=True)
    except subprocess.CalledProcessError:
        print("Nothing to commit for:", commit_msg)
    # Push changes
    subprocess.run(["git", "-C", REPO_DIR, "push"], check=True)

def read_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        return f.read()

def write_readme(content):
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

content = read_readme()

# 1. SaaS products column and sort
saas_data = [
    ("| **[Google Analytics 4 (GA4)](https://analytics.google.com/)** | Free event-based analytics from Google with strong integration ecosystem. | Free (GA4) / Custom (360) | Unlimited (Standard) |", 2000000, "$2T (Alphabet)"),
    ("| **[Contentsquare](https://contentsquare.com/)** | Digital experience analytics with session replay and zone-based insights. | Custom pricing | No free tier |", 5600, "$5.6B"),
    ("| **[Pendo](https://www.pendo.io/)** | Product experience platform with in-app guidance and analytics. | Custom pricing | 500 MAU |", 2600, "$2.6B"),
    ("| **[FullStory](https://www.fullstory.com/)** | Session replay and behavioral analytics platform with AI insights. | Custom pricing | 1,000 sessions/month |", 1800, "$1.8B"),
    ("| **[Amplitude](https://amplitude.com/)** | Comprehensive product analytics with advanced behavioral cohort analysis and predictive features. | Starts at $49/mo | 10M events/month |", 1300, "$1.3B"),
    ("| **[Mixpanel](https://mixpanel.com/)** | Leading event-based analytics platform with strong user behavior insights and AI features. | Starts at $20/mo | 20M events/month |", 1050, "$1.05B"),
    ("| **[Heap](https://heap.io/)** | Automatic event capture and retroactive analysis platform. | Custom pricing | 10k sessions/month |", 1000, "$1B+ (Acquired)"),
    ("| **[PostHog](https://posthog.com/)** | Open-source-friendly product analytics with session replay and feature flags. | Pay as you go | 1M events/month |", 500, "$500M+"),
    ("| **[Moesif](https://www.moesif.com/)** | API analytics and product analytics for developers with strong event tracking. | Starts at $85/mo | 500,000 events/month |", 50, "$50M+"),
    ("| **[Matomo](https://matomo.org/)** | Privacy-focused analytics platform with full data ownership. | Starts at €19/mo (Cloud) | Self-hosted is Free |", 20, "$20M+ (Revenue)"),
    ("| **[OpenPanel](https://openpanel.com/)** | Privacy-first analytics platform with event tracking and user journey visualization. | Starts at $50/mo | 100k events/month |", 5, "<$10M"),
]

saas_data.sort(key=lambda x: x[1], reverse=True)

new_table = "| Product | Description | Pricing | Free Tier Limit | Company Size |\n"
new_table += "|---------|-------------|---------|-----------------|--------------|\n"
for row, _, size_str in saas_data:
    new_table += row + f" {size_str} |\n"

# Replace the table in content
content = re.sub(r"\| Product \| Description \| Pricing \| Free Tier Limit \|\n\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+", new_table, content, flags=re.DOTALL)
# Actually the previous table has exact hyphens: |---------|-------------|---------|-----------------|
content = re.sub(r"\| Product \| Description \| Pricing \| Free Tier Limit \|\n\|--.*?\n(?:\|.*?\|\n)+", new_table, content, flags=re.DOTALL)
write_readme(content)
run_git("Added company size and sorted the SaaS based on that")

# 2. Open source repos badge and sort
content = read_readme()
os_repos = [
    ("- **[Superset](https://github.com/apache/superset)** — Apache Superset for data exploration and visualization.", 59000, "apache/superset"),
    ("- **[Metabase](https://github.com/metabase/metabase)** — Open-source business intelligence for analyzing event data.", 36000, "metabase/metabase"),
    ("- **[Matomo](https://github.com/matomo-org/matomo)**  \n  Leading open-source analytics platform with full event tracking, heatmaps, and data ownership.", 20000, "matomo-org/matomo"),
    ("- **[PostHog](https://github.com/PostHog/posthog)**  \n  Complete open-source product analytics platform with event tracking, session replay, feature flags, and A/B testing.", 18000, "PostHog/posthog"),
    ("- **[Plausible](https://github.com/plausible/analytics)**  \n  Lightweight, privacy-first open-source analytics alternative focused on simplicity.", 18000, "plausible/analytics"),
    ("- **[Umami](https://github.com/umami-software/umami)**  \n  Simple and elegant open-source website analytics with event tracking.", 20000, "umami-software/umami"),
    ("- **[Redash](https://github.com/getredash/redash)** — Open-source data visualization and querying tool.", 25000, "getredash/redash"),
    ("- **[OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification)**  \n  Industry-standard observability framework for collecting events and traces across applications.", 15000, "open-telemetry/opentelemetry-specification"),
    ("- **[Snowplow](https://github.com/snowplow/snowplow)**  \n  Open-source behavioral data platform with rich event modeling and real-time processing.", 8000, "snowplow/snowplow"),
    ("- **[Fathom](https://github.com/usefathom/fathom)**  \n  Privacy-focused open-source analytics with minimal tracking.", 7000, "usefathom/fathom"),
    ("- **[Ackee](https://github.com/ackee/ackee)**  \n  Open-source analytics tool with a focus on privacy and clean interface.", 4000, "ackee/ackee"),
    ("- **[RudderStack](https://github.com/rudderlabs/rudder-server)**  \n  Open-source customer data platform for collecting and routing events to multiple destinations.", 4000, "rudderlabs/rudder-server"),
    ("- **[Shynet](https://github.com/milesmcc/shynet)**  \n  Self-hosted, privacy-respecting analytics platform.", 3000, "milesmcc/shynet"),
]
# We will just replace the two OS sections with one sorted list for simplicity, or just replace all matches in the text.
# Let's replace the whole Open-Source GitHub Projects section.
os_repos.sort(key=lambda x: x[1], reverse=True)

os_section = "## Open-Source GitHub Projects\n\n"
for line, stars, repo in os_repos:
    badge = f"[![Stars](https://img.shields.io/github/stars/{repo}?style=social&color=white)](https://github.com/{repo}/stargazers)"
    # Insert badge after the repo link
    line = re.sub(r"(\*\*\[.*?\]\(.*?\)\*\*)", r"\1 " + badge, line)
    os_section += line + "\n\n"

os_section += "- **[LangGraph Analytics Agents]** for building custom AI-powered insights.\n"
os_section += "- **[n8n]** workflows for event processing and automation.\n"
os_section += "- Many community **self-hosted PostHog** and **Matomo** deployments.\n\n"
os_section += "**Frameworks for building custom analytics**: Combine **PostHog**, **Snowplow**, **RudderStack**, and **OpenTelemetry** with **Metabase** or **Superset** for a complete open-source event analytics stack.\n"

content = re.sub(r"## Open-Source GitHub Projects\n\n.*?\n## How to Contribute", os_section + "## How to Contribute", content, flags=re.DOTALL)
write_readme(content)
run_git("Added github stars and sorted the opensource based on that")

# 3. Banner
content = read_readme()
banner = '<p align="center">\n  <img src="assets/banner.svg" alt="Awesome Event-Based Product Analytics" width="100%">\n</p>\n\n'
if banner not in content:
    content = banner + content
write_readme(content)
run_git("added banner")

# 4. Emojis
content = read_readme()
content = content.replace("# Awesome-Event-Based-Product-Analytics", "# 🚀 Awesome-Event-Based-Product-Analytics")
content = content.replace("## Top Event-Based Product Analytics Tools Ecosystem", "## 🌟 Top Event-Based Product Analytics Tools Ecosystem")
content = content.replace("## Table of Contents", "## 📑 Table of Contents")
content = content.replace("## SaaS Products", "## ☁️ SaaS Products")
content = content.replace("## Open-Source GitHub Projects", "## 🌐 Open-Source GitHub Projects")
content = content.replace("## How to Contribute", "## 🤝 How to Contribute")
content = content.replace("## Disclaimer", "## ⚠️ Disclaimer")
write_readme(content)
run_git("added emojis")

# 5. SEO
content = read_readme()
seo_block = "\n<!-- SEO Keywords: product analytics, event tracking, user behavior, analytics tools, mixpanel, amplitude, open source analytics, posthog, ga4, SaaS analytics, cohort analysis -->\n"
if "SEO Keywords" not in content:
    content = content.replace("# 🚀 Awesome-Event-Based-Product-Analytics\n", "# 🚀 Awesome-Event-Based-Product-Analytics\n" + seo_block)
write_readme(content)
run_git("seo optimised")

# 6. Badges left
content = read_readme()
badge_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
# Let's put badges at the top, just under the banner
if 'alt="Discord"' not in content:
    content = content.replace(seo_block, seo_block + "\n" + badge_left + "\n")
write_readme(content)
run_git("badges to left added")

# 7. Badges right
content = read_readme()
badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
content = content.replace(badge_left, badge_left + " " + badge_right)
write_readme(content)
run_git("badges to right added")

# 8. Star history
content = read_readme()
star_history = """
## 📈 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Event-Based-Product-Analytics&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Event-Based-Product-Analytics&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Event-Based-Product-Analytics&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Event-Based-Product-Analytics&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
if "Star History Chart" not in content:
    content += "\n" + star_history
write_readme(content)
run_git("star history added")

# 9. Replace chartrepos with chart?repos
content = read_readme()
content = content.replace("chartrepos", "chart?repos")
write_readme(content)
run_git("fixed star plot")

# 10. Replace awesome link
content = read_readme()
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
write_readme(content)
run_git("invalid awesome link fixed")

print("All tasks completed successfully!")
