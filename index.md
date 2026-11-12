---
title: Schedule
layout: home
nav_order: 1
---

# Foundations of Machine Learning
{: .fs-9 }

DS 3001 / DS 3021 · University of Virginia
{: .fs-6 .fw-300 }

[Get set up]({{ "/setup/" | relative_url }}){: .btn .btn-primary .mr-2 }
[View on GitHub](https://github.com/{{ site.repo }}){: .btn }

---

Each week has three sessions:

- **Monday:** math lecture (no computers)
- **Wednesday:** hands-on coding
- **Friday:** lab

Coding sessions link to the lecture slides and the notebook on GitHub. See [Setup]({{ "/setup/" | relative_url }}) to download the datasets first.

{% for unit in site.data.schedule %}
## {{ unit.unit }}

<table>
  <thead>
    <tr><th style="width:8rem">Date</th><th>Topic</th><th style="width:15rem">Materials</th></tr>
  </thead>
  <tbody>
  {%- for s in unit.sessions %}
    <tr>
      <td>{{ s.date }}</td>
      <td>
        {%- if s.type == "lab" or s.type == "project" -%}<span class="label label-uva">Lab</span> {{ s.topic }}
        {%- elsif s.type == "break" -%}<em>{{ s.topic }}</em>
        {%- else -%}{{ s.topic }}{%- endif -%}
      </td>
      <td>
        {%- if s.lecture -%}{% include lecture_links.html id=s.lecture %}{%- endif -%}
        {%- for x in s.also -%}<br><a href="{{ 'lectures/' | append: x | append: '/' | append: x | append: '.slides.html' | relative_url }}">{{ x }} slides</a>{%- endfor -%}
      </td>
    </tr>
  {%- endfor %}
  </tbody>
</table>
{% endfor %}
