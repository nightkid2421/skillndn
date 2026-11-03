# Third-party notices

This repository collects skill folders from an installed environment. Ownership remains with the respective authors. Original instructions and copyright notices are preserved. The root license covers only newly authored packaging scripts and repository documentation.

| Skill group | Original source | License evidence |
|---|---|---|
| imagegen, openai-docs, skill-creator, skill-installer | OpenAI Codex system skills | Apache-2.0 license text preserved inside each skill folder |
| create-agent-adapter, paperclip, paperclip-create-agent, para-memory-files | [paperclipai/paperclip](https://github.com/paperclipai/paperclip), installed via @paperclipai/adapter-codex-local 0.3.1 | Upstream [MIT license](https://github.com/paperclipai/paperclip/blob/master/LICENSE), preserved inside each skill folder |
| pdf | OpenAI PDF plugin 26.1026.10807 | Original plugin manifest declaring MIT: [license evidence](licenses/pdf-plugin.json) |
| presentations | OpenAI Presentations plugin 26.1026.10807 | Original plugin manifest declaring MIT: [license evidence](licenses/presentations-plugin.json); original code copyright headers retained |
| spreadsheets, excel-live-control | OpenAI Spreadsheets plugin 26.1026.10807 | Original plugin manifest declaring MIT: [license evidence](licenses/spreadsheets-plugin.json) |

For the MIT-declared OpenAI plugin materials, retain their original OpenAI attribution and the following MIT permission terms with copies. These terms are provided from the standard MIT license; the original declaration is preserved in the evidence files above.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Exclusions

See [CATALOG.md](CATALOG.md) for every detected skill and its inclusion decision. In particular, Documents has an explicit skill-level license restricting extraction and redistribution despite an MIT field in its plugin manifest, so its contents are excluded. Proprietary plugins and skills without an explicit redistribution license are also excluded. No proprietary runtime binaries, account configuration, credentials or personal memory stores are included.
