---
title: Lectures
nav_order: 3
---

# Lectures

All lecture notebooks in order, with the datasets each one uses from `data/`.

<table>
  <thead>
    <tr><th style="width:3rem">#</th><th>Lecture</th><th>Datasets</th><th style="width:15rem">Materials</th></tr>
  </thead>
  <tbody>
  {%- for l in site.data.lectures %}
    <tr>
      <td>{{ l.id | slice: 0, 2 }}</td>
      <td>{{ l.title }}</td>
      <td>{% if l.data != "" %}<code>{{ l.data | replace: ", ", "</code>, <code>" }}</code>{% else %}—{% endif %}</td>
      <td>{% include lecture_links.html id=l.id %}</td>
    </tr>
  {%- endfor %}
  </tbody>
</table>
