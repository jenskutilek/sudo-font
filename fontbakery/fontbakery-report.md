## FontBakery report

fontbakery version: 0.13.2







## Check results



<details><summary>[2] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-consistent-family-name">opentype/family/consistent_family_name</a></summary>
    <div>







* 🔥 **FAIL** <p>2 different Font Family names were found:</p>
<ul>
<li>
<p>'Sudo' was found in:</p>
<ul>
<li>Sudo[YTDE,wght].ttf (nameID 1)</li>
<li>Sudo-Italic[YTDE,wght].ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Sudo UI' was found in:</p>
<ul>
<li>SudoUI-Italic[YTDE,wght].ttf (nameID 1)</li>
<li>SudoUI[YTDE,wght].ttf (nameID 1)</li>
</ul>
</li>
</ul>
 [code: inconsistent-family-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Each font in a family must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-vertical-metrics">family/vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>sTypoAscender is not the same across the family:
Sudo: 832
Sudo UI Italic: 896
Sudo UI: 896
Sudo Italic: 832</p>
 [code: sTypoAscender-mismatch]



* 🔥 **FAIL** <p>ascent is not the same across the family:
Sudo: 832
Sudo UI Italic: 896
Sudo UI: 896
Sudo Italic: 832</p>
 [code: ascent-mismatch]



</div>
</details>
</div>
</details>

<details><summary>[10] Sudo[YTDE,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: e̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: E̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: é̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: É̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: è̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: È̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: o̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: O̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: s̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: S̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* 🔥 **FAIL** <p>The defaul value YTDE:-231.0 is not registered as an axis fallback name on the Google Axis Registry.
You should consider suggesting the addition of this value to the registry or adopted one of the existing fallback names for this axis:
[name: &quot;Normal&quot;
value: -250.0
]</p>
 [code: not-registered]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>Axis Value for 'YTDE':'Normal' is expected to be '-250.0' but this font has 'Normal'='-231.0'.</p>
 [code: bad-coordinate]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 803 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ⚠️ **WARN** <p>In order to optimize performance on some legacy renderers, the value of unitsPerEm at the head table should ideally be a power of 2 between 16 to 16384. And values of 1000 and 2000 are also common and may be just fine as well. But we got 832 instead.</p>
 [code: suboptimal]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>There is only one CJK glyph when there needs to be at least 150 in order to support the smallest CJK writing system, Kana.
The following CJK glyphs were found:
['uni33D1']
Please check that these glyphs have the correct unicodes.</p>
 [code: cjk-not-enough-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni019D (U+019D): L&lt;&lt;132.0,0.0&gt;--&lt;60.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0253 (U+0253): L&lt;&lt;132.0,512.0&gt;--&lt;60.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0257 (U+0257): L&lt;&lt;388.0,512.0&gt;--&lt;316.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0199 (U+0199): L&lt;&lt;132.0,512.0&gt;--&lt;60.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0272 (U+0272): L&lt;&lt;132.0,0.0&gt;--&lt;60.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01B4 (U+01B4): L&lt;&lt;318.0,448.0&gt;--&lt;390.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;158.0,35.0&gt;--&lt;214.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;258.0,35.0&gt;--&lt;314.0,35.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, coptic, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, gothic, glagolitic, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, syriac, old-permic, tai-le, coptic, duployan, math, tifinagh, todhri, canadian-aboriginal, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: sunuwar, math</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, syriac, cherokee, tifinagh, sunuwar, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, hatran, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, old-hungarian, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A5 UPWARDS ARROW FROM BAR: try adding math</li>
<li>U+21A8 UP DOWN ARROW WITH BASE: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2204 THERE DOES NOT EXIST: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2216 SET MINUS: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, tai-tham, symbols, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+221F RIGHT ANGLE: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2236 RATIO: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2259 ESTIMATES: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+2302 HOUSE: try adding symbols</li>
<li>U+2310 REVERSED NOT SIGN: try adding math</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2320 TOP HALF INTEGRAL: try adding math</li>
<li>U+2321 BOTTOM HALF INTEGRAL: try adding math</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23ED BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23EE BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23F5 BLACK MEDIUM RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+2400 SYMBOL FOR NULL: try adding symbols</li>
<li>U+2401 SYMBOL FOR START OF HEADING: try adding symbols</li>
<li>U+2402 SYMBOL FOR START OF TEXT: try adding symbols</li>
<li>U+2403 SYMBOL FOR END OF TEXT: try adding symbols</li>
<li>U+2404 SYMBOL FOR END OF TRANSMISSION: try adding symbols</li>
<li>U+2405 SYMBOL FOR ENQUIRY: try adding symbols</li>
<li>U+2406 SYMBOL FOR ACKNOWLEDGE: try adding symbols</li>
<li>U+2407 SYMBOL FOR BELL: try adding symbols</li>
<li>U+2408 SYMBOL FOR BACKSPACE: try adding symbols</li>
<li>U+2409 SYMBOL FOR HORIZONTAL TABULATION: try adding symbols</li>
<li>U+240A SYMBOL FOR LINE FEED: try adding symbols</li>
<li>U+240B SYMBOL FOR VERTICAL TABULATION: try adding symbols</li>
<li>U+240C SYMBOL FOR FORM FEED: try adding symbols</li>
<li>U+240D SYMBOL FOR CARRIAGE RETURN: try adding symbols</li>
<li>U+240E SYMBOL FOR SHIFT OUT: try adding symbols</li>
<li>U+240F SYMBOL FOR SHIFT IN: try adding symbols</li>
<li>U+2410 SYMBOL FOR DATA LINK ESCAPE: try adding symbols</li>
<li>U+2411 SYMBOL FOR DEVICE CONTROL ONE: try adding symbols</li>
<li>U+2412 SYMBOL FOR DEVICE CONTROL TWO: try adding symbols</li>
<li>U+2413 SYMBOL FOR DEVICE CONTROL THREE: try adding symbols</li>
<li>U+2414 SYMBOL FOR DEVICE CONTROL FOUR: try adding symbols</li>
<li>U+2415 SYMBOL FOR NEGATIVE ACKNOWLEDGE: try adding symbols</li>
<li>U+2416 SYMBOL FOR SYNCHRONOUS IDLE: try adding symbols</li>
<li>U+2417 SYMBOL FOR END OF TRANSMISSION BLOCK: try adding symbols</li>
<li>U+2418 SYMBOL FOR CANCEL: try adding symbols</li>
<li>U+2419 SYMBOL FOR END OF MEDIUM: try adding symbols</li>
<li>U+241A SYMBOL FOR SUBSTITUTE: try adding symbols</li>
<li>U+241B SYMBOL FOR ESCAPE: try adding symbols</li>
<li>U+241C SYMBOL FOR FILE SEPARATOR: try adding symbols</li>
<li>U+241D SYMBOL FOR GROUP SEPARATOR: try adding symbols</li>
<li>U+241E SYMBOL FOR RECORD SEPARATOR: try adding symbols</li>
<li>U+241F SYMBOL FOR UNIT SEPARATOR: try adding symbols</li>
<li>U+2420 SYMBOL FOR SPACE: try adding symbols</li>
<li>U+2421 SYMBOL FOR DELETE: try adding symbols</li>
<li>U+2424 SYMBOL FOR NEWLINE: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25A7 SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL: try adding symbols</li>
<li>U+25A8 SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25AC BLACK RECTANGLE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BB WHITE RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C5 WHITE LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: cham, lepcha, chakma, bengali, newa, mongolian, yi, gunjala-gondi, miao, tifinagh, modi, limbu, osage, telugu, thai, tagbanwa, buginese, duployan, siddham, psalter-pahlavi, manichaean, armenian, caucasian-albanian, sogdian, bassa-vah, elbasan, lao, warang-citi, saurashtra, pahawh-hmong, tamil, kayah-li, grantha, mahajani, rejang, syloti-nagri, syriac, adlam, wancho, tai-viet, hanifi-rohingya, tai-le, soyombo, nko, khmer, phags-pa, khojki, hanunoo, mende-kikakui, ahom, tai-tham, new-tai-lue, devanagari, buhid, tibetan, masaram-gondi, coptic, symbols, tagalog, thaana, gujarati, kannada, sharada, sinhala, marchen, canadian-aboriginal, oriya, javanese, kaithi, myanmar, old-permic, meetei-mayek, brahmi, gurmukhi, tirhuta, batak, takri, balinese, kharoshthi, malayalam, dogra, sundanese, math, zanabazar-square, bhaiksuki, music, mandaic, khudawadi, hebrew</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D8 INVERSE BULLET: try adding symbols</li>
<li>U+25D9 INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25E2 BLACK LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E3 BLACK LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E4 BLACK UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E5 BLACK UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2601 CLOUD: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2610 BALLOT BOX: try adding symbols</li>
<li>U+2611 BALLOT BOX WITH CHECK: try adding symbols</li>
<li>U+2612 BALLOT BOX WITH X: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2639 WHITE FROWNING FACE: try adding symbols</li>
<li>U+263A WHITE SMILING FACE: try adding symbols</li>
<li>U+263B BLACK SMILING FACE: try adding symbols</li>
<li>U+263C WHITE SUN WITH RAYS: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2660 BLACK SPADE SUIT: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2663 BLACK CLUB SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2666 BLACK DIAMOND SUIT: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+2690 WHITE FLAG: try adding symbols</li>
<li>U+2691 BLACK FLAG: try adding symbols</li>
<li>U+26ED GEAR WITHOUT HUB: try adding symbols</li>
<li>U+2709 ENVELOPE: try adding symbols</li>
<li>U+270E LOWER RIGHT PENCIL: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2714 HEAVY CHECK MARK: try adding symbols</li>
<li>U+2715 MULTIPLICATION X: try adding symbols</li>
<li>U+2716 HEAVY MULTIPLICATION X: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2718 HEAVY BALLOT X: try adding symbols</li>
<li>U+271A HEAVY GREEK CROSS: try adding symbols</li>
<li>U+276E HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+276F HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+27C2 PERPENDICULAR: try adding math</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+2800 BRAILLE PATTERN BLANK: try adding one of: braille, symbols</li>
<li>U+2801 BRAILLE PATTERN DOTS-1: try adding one of: braille, symbols</li>
<li>U+2802 BRAILLE PATTERN DOTS-2: try adding one of: braille, symbols</li>
<li>U+2803 BRAILLE PATTERN DOTS-12: try adding one of: braille, symbols</li>
<li>U+2804 BRAILLE PATTERN DOTS-3: try adding one of: braille, symbols</li>
<li>U+2805 BRAILLE PATTERN DOTS-13: try adding one of: braille, symbols</li>
<li>U+2806 BRAILLE PATTERN DOTS-23: try adding one of: braille, symbols</li>
<li>U+2807 BRAILLE PATTERN DOTS-123: try adding one of: braille, symbols</li>
<li>U+2808 BRAILLE PATTERN DOTS-4: try adding one of: braille, symbols</li>
<li>U+2809 BRAILLE PATTERN DOTS-14: try adding one of: braille, symbols</li>
<li>U+280A BRAILLE PATTERN DOTS-24: try adding one of: braille, symbols</li>
<li>U+280B BRAILLE PATTERN DOTS-124: try adding one of: braille, symbols</li>
<li>U+280C BRAILLE PATTERN DOTS-34: try adding one of: braille, symbols</li>
<li>U+280D BRAILLE PATTERN DOTS-134: try adding one of: braille, symbols</li>
<li>U+280E BRAILLE PATTERN DOTS-234: try adding one of: braille, symbols</li>
<li>U+280F BRAILLE PATTERN DOTS-1234: try adding one of: braille, symbols</li>
<li>U+2810 BRAILLE PATTERN DOTS-5: try adding one of: braille, symbols</li>
<li>U+2811 BRAILLE PATTERN DOTS-15: try adding one of: braille, symbols</li>
<li>U+2812 BRAILLE PATTERN DOTS-25: try adding one of: braille, symbols</li>
<li>U+2813 BRAILLE PATTERN DOTS-125: try adding one of: braille, symbols</li>
<li>U+2814 BRAILLE PATTERN DOTS-35: try adding one of: braille, symbols</li>
<li>U+2815 BRAILLE PATTERN DOTS-135: try adding one of: braille, symbols</li>
<li>U+2816 BRAILLE PATTERN DOTS-235: try adding one of: braille, symbols</li>
<li>U+2817 BRAILLE PATTERN DOTS-1235: try adding one of: braille, symbols</li>
<li>U+2818 BRAILLE PATTERN DOTS-45: try adding one of: braille, symbols</li>
<li>U+2819 BRAILLE PATTERN DOTS-145: try adding one of: braille, symbols</li>
<li>U+281A BRAILLE PATTERN DOTS-245: try adding one of: braille, symbols</li>
<li>U+281B BRAILLE PATTERN DOTS-1245: try adding one of: braille, symbols</li>
<li>U+281C BRAILLE PATTERN DOTS-345: try adding one of: braille, symbols</li>
<li>U+281D BRAILLE PATTERN DOTS-1345: try adding one of: braille, symbols</li>
<li>U+281E BRAILLE PATTERN DOTS-2345: try adding one of: braille, symbols</li>
<li>U+281F BRAILLE PATTERN DOTS-12345: try adding one of: braille, symbols</li>
<li>U+2820 BRAILLE PATTERN DOTS-6: try adding one of: braille, symbols</li>
<li>U+2821 BRAILLE PATTERN DOTS-16: try adding one of: braille, symbols</li>
<li>U+2822 BRAILLE PATTERN DOTS-26: try adding one of: braille, symbols</li>
<li>U+2823 BRAILLE PATTERN DOTS-126: try adding one of: braille, symbols</li>
<li>U+2824 BRAILLE PATTERN DOTS-36: try adding one of: braille, symbols</li>
<li>U+2825 BRAILLE PATTERN DOTS-136: try adding one of: braille, symbols</li>
<li>U+2826 BRAILLE PATTERN DOTS-236: try adding one of: braille, symbols</li>
<li>U+2827 BRAILLE PATTERN DOTS-1236: try adding one of: braille, symbols</li>
<li>U+2828 BRAILLE PATTERN DOTS-46: try adding one of: braille, symbols</li>
<li>U+2829 BRAILLE PATTERN DOTS-146: try adding one of: braille, symbols</li>
<li>U+282A BRAILLE PATTERN DOTS-246: try adding one of: braille, symbols</li>
<li>U+282B BRAILLE PATTERN DOTS-1246: try adding one of: braille, symbols</li>
<li>U+282C BRAILLE PATTERN DOTS-346: try adding one of: braille, symbols</li>
<li>U+282D BRAILLE PATTERN DOTS-1346: try adding one of: braille, symbols</li>
<li>U+282E BRAILLE PATTERN DOTS-2346: try adding one of: braille, symbols</li>
<li>U+282F BRAILLE PATTERN DOTS-12346: try adding one of: braille, symbols</li>
<li>U+2830 BRAILLE PATTERN DOTS-56: try adding one of: braille, symbols</li>
<li>U+2831 BRAILLE PATTERN DOTS-156: try adding one of: braille, symbols</li>
<li>U+2832 BRAILLE PATTERN DOTS-256: try adding one of: braille, symbols</li>
<li>U+2833 BRAILLE PATTERN DOTS-1256: try adding one of: braille, symbols</li>
<li>U+2834 BRAILLE PATTERN DOTS-356: try adding one of: braille, symbols</li>
<li>U+2835 BRAILLE PATTERN DOTS-1356: try adding one of: braille, symbols</li>
<li>U+2836 BRAILLE PATTERN DOTS-2356: try adding one of: braille, symbols</li>
<li>U+2837 BRAILLE PATTERN DOTS-12356: try adding one of: braille, symbols</li>
<li>U+2838 BRAILLE PATTERN DOTS-456: try adding one of: braille, symbols</li>
<li>U+2839 BRAILLE PATTERN DOTS-1456: try adding one of: braille, symbols</li>
<li>U+283A BRAILLE PATTERN DOTS-2456: try adding one of: braille, symbols</li>
<li>U+283B BRAILLE PATTERN DOTS-12456: try adding one of: braille, symbols</li>
<li>U+283C BRAILLE PATTERN DOTS-3456: try adding one of: braille, symbols</li>
<li>U+283D BRAILLE PATTERN DOTS-13456: try adding one of: braille, symbols</li>
<li>U+283E BRAILLE PATTERN DOTS-23456: try adding one of: braille, symbols</li>
<li>U+283F BRAILLE PATTERN DOTS-123456: try adding one of: braille, symbols</li>
<li>U+2913 DOWNWARDS ARROW TO BAR: try adding math</li>
<li>U+2940 ANTICLOCKWISE CLOSED CIRCLE ARROW: try adding math</li>
<li>U+2B51 BLACK SMALL STAR: try adding symbols</li>
<li>U+2B52 WHITE SMALL STAR: try adding symbols</li>
<li>U+2BBD BALLOT BOX WITH LIGHT X: try adding symbols</li>
<li>U+2BE8 LEFT HALF BLACK STAR: try adding symbols</li>
<li>U+2BE9 RIGHT HALF BLACK STAR: try adding symbols</li>
<li>U+2BEA STAR WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+2BEB STAR WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+33D1 SQUARE LN: not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0A3 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+EC00 : not included in any glyphset definition</li>
<li>U+EC01 : not included in any glyphset definition</li>
<li>U+EC02 : not included in any glyphset definition</li>
<li>U+EC03 : not included in any glyphset definition</li>
<li>U+EC07 : not included in any glyphset definition</li>
<li>U+EC08 : not included in any glyphset definition</li>
<li>U+EC09 : not included in any glyphset definition</li>
<li>U+EC0A : not included in any glyphset definition</li>
<li>U+EC25 : not included in any glyphset definition</li>
<li>U+EC26 : not included in any glyphset definition</li>
<li>U+EC27 : not included in any glyphset definition</li>
<li>U+EC28 : not included in any glyphset definition</li>
<li>U+EC2A : not included in any glyphset definition</li>
<li>U+EC2B : not included in any glyphset definition</li>
<li>U+EC2C : not included in any glyphset definition</li>
<li>U+EC2E : not included in any glyphset definition</li>
<li>U+EC2F : not included in any glyphset definition</li>
<li>U+1F319 CRESCENT MOON: not included in any glyphset definition</li>
<li>U+1F327 CLOUD WITH RAIN: try adding symbols</li>
<li>U+1F3E0 HOUSE BUILDING: try adding symbols</li>
<li>U+1F44D THUMBS UP SIGN: try adding symbols</li>
<li>U+1F44E THUMBS DOWN SIGN: try adding symbols</li>
<li>U+1F464 BUST IN SILHOUETTE: not included in any glyphset definition</li>
<li>U+1F4AC SPEECH BALLOON: not included in any glyphset definition</li>
<li>U+1F4BE FLOPPY DISK: not included in any glyphset definition</li>
<li>U+1F4C0 DVD: not included in any glyphset definition</li>
<li>U+1F4C1 FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C2 OPEN FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C6 TEAR-OFF CALENDAR: not included in any glyphset definition</li>
<li>U+1F4DE TELEPHONE RECEIVER: not included in any glyphset definition</li>
<li>U+1F4F1 MOBILE PHONE: not included in any glyphset definition</li>
<li>U+1F4F6 ANTENNA WITH BARS: not included in any glyphset definition</li>
<li>U+1F500 TWISTED RIGHTWARDS ARROWS: not included in any glyphset definition</li>
<li>U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS: not included in any glyphset definition</li>
<li>U+1F508 SPEAKER: try adding symbols</li>
<li>U+1F50A SPEAKER WITH THREE SOUND WAVES: try adding symbols</li>
<li>U+1F50D LEFT-POINTING MAGNIFYING GLASS: try adding symbols</li>
<li>U+1F50E RIGHT-POINTING MAGNIFYING GLASS: not included in any glyphset definition</li>
<li>U+1F511 KEY: not included in any glyphset definition</li>
<li>U+1F512 LOCK: try adding symbols</li>
<li>U+1F513 OPEN LOCK: try adding symbols</li>
<li>U+1F5A4 BLACK HEART: try adding symbols</li>
<li>U+1F5C0 FOLDER: try adding symbols</li>
<li>U+1F5C1 OPEN FOLDER: try adding symbols</li>
<li>U+1F5D1 WASTEBASKET: try adding symbols</li>
<li>U+1F5D5 MINIMIZE: try adding symbols</li>
<li>U+1F5D6 MAXIMIZE: try adding symbols</li>
<li>U+1F5D8 CLOCKWISE RIGHT AND LEFT SEMICIRCLE ARROWS: try adding symbols</li>
<li>U+1F5F4 BALLOT SCRIPT X: try adding symbols</li>
<li>U+1F5F5 BALLOT BOX WITH SCRIPT X: try adding symbols</li>
<li>U+1F5F6 BALLOT BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F7 BALLOT BOX WITH BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F9 BALLOT BOX WITH BOLD CHECK: try adding symbols</li>
<li>U+1F600 GRINNING FACE: not included in any glyphset definition</li>
<li>U+1F601 GRINNING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F60A SMILING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F620 ANGRY FACE: not included in any glyphset definition</li>
<li>U+1F621 POUTING FACE: not included in any glyphset definition</li>
<li>U+1F6C9 BOYS SYMBOL: try adding symbols</li>
<li>U+1F6CA GIRLS SYMBOL: try adding symbols</li>
<li>U+1F6D2 SHOPPING TROLLEY: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[10] Sudo-Italic[YTDE,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: e̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: E̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: é̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: É̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: è̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: È̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: o̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: O̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: s̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: S̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* 🔥 **FAIL** <p>The defaul value YTDE:-231.0 is not registered as an axis fallback name on the Google Axis Registry.
You should consider suggesting the addition of this value to the registry or adopted one of the existing fallback names for this axis:
[name: &quot;Normal&quot;
value: -250.0
]</p>
 [code: not-registered]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>Axis Value for 'YTDE':'Normal' is expected to be '-250.0' but this font has 'Normal'='-231.0'.</p>
 [code: bad-coordinate]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 792 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ⚠️ **WARN** <p>In order to optimize performance on some legacy renderers, the value of unitsPerEm at the head table should ideally be a power of 2 between 16 to 16384. And values of 1000 and 2000 are also common and may be just fine as well. But we got 832 instead.</p>
 [code: suboptimal]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>There is only one CJK glyph when there needs to be at least 150 in order to support the smallest CJK writing system, Kana.
The following CJK glyphs were found:
['uni33D1']
Please check that these glyphs have the correct unicodes.</p>
 [code: cjk-not-enough-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni019D (U+019D): L&lt;&lt;87.0,0.0&gt;--&lt;15.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0253 (U+0253): L&lt;&lt;190.0,512.0&gt;--&lt;118.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0257 (U+0257): L&lt;&lt;446.0,512.0&gt;--&lt;374.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0199 (U+0199): L&lt;&lt;190.0,512.0&gt;--&lt;118.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0272 (U+0272): L&lt;&lt;87.0,0.0&gt;--&lt;15.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01B4 (U+01B4): L&lt;&lt;363.0,448.0&gt;--&lt;435.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;120.0,35.0&gt;--&lt;176.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;220.0,35.0&gt;--&lt;276.0,35.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, coptic, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, gothic, glagolitic, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, syriac, old-permic, tai-le, coptic, duployan, math, tifinagh, todhri, canadian-aboriginal, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: sunuwar, math</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, syriac, cherokee, tifinagh, sunuwar, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, hatran, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, old-hungarian, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A5 UPWARDS ARROW FROM BAR: try adding math</li>
<li>U+21A8 UP DOWN ARROW WITH BASE: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2204 THERE DOES NOT EXIST: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2216 SET MINUS: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, tai-tham, symbols, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+221F RIGHT ANGLE: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2236 RATIO: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2259 ESTIMATES: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+2302 HOUSE: try adding symbols</li>
<li>U+2310 REVERSED NOT SIGN: try adding math</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2320 TOP HALF INTEGRAL: try adding math</li>
<li>U+2321 BOTTOM HALF INTEGRAL: try adding math</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23ED BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23EE BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23F5 BLACK MEDIUM RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+2400 SYMBOL FOR NULL: try adding symbols</li>
<li>U+2401 SYMBOL FOR START OF HEADING: try adding symbols</li>
<li>U+2402 SYMBOL FOR START OF TEXT: try adding symbols</li>
<li>U+2403 SYMBOL FOR END OF TEXT: try adding symbols</li>
<li>U+2404 SYMBOL FOR END OF TRANSMISSION: try adding symbols</li>
<li>U+2405 SYMBOL FOR ENQUIRY: try adding symbols</li>
<li>U+2406 SYMBOL FOR ACKNOWLEDGE: try adding symbols</li>
<li>U+2407 SYMBOL FOR BELL: try adding symbols</li>
<li>U+2408 SYMBOL FOR BACKSPACE: try adding symbols</li>
<li>U+2409 SYMBOL FOR HORIZONTAL TABULATION: try adding symbols</li>
<li>U+240A SYMBOL FOR LINE FEED: try adding symbols</li>
<li>U+240B SYMBOL FOR VERTICAL TABULATION: try adding symbols</li>
<li>U+240C SYMBOL FOR FORM FEED: try adding symbols</li>
<li>U+240D SYMBOL FOR CARRIAGE RETURN: try adding symbols</li>
<li>U+240E SYMBOL FOR SHIFT OUT: try adding symbols</li>
<li>U+240F SYMBOL FOR SHIFT IN: try adding symbols</li>
<li>U+2410 SYMBOL FOR DATA LINK ESCAPE: try adding symbols</li>
<li>U+2411 SYMBOL FOR DEVICE CONTROL ONE: try adding symbols</li>
<li>U+2412 SYMBOL FOR DEVICE CONTROL TWO: try adding symbols</li>
<li>U+2413 SYMBOL FOR DEVICE CONTROL THREE: try adding symbols</li>
<li>U+2414 SYMBOL FOR DEVICE CONTROL FOUR: try adding symbols</li>
<li>U+2415 SYMBOL FOR NEGATIVE ACKNOWLEDGE: try adding symbols</li>
<li>U+2416 SYMBOL FOR SYNCHRONOUS IDLE: try adding symbols</li>
<li>U+2417 SYMBOL FOR END OF TRANSMISSION BLOCK: try adding symbols</li>
<li>U+2418 SYMBOL FOR CANCEL: try adding symbols</li>
<li>U+2419 SYMBOL FOR END OF MEDIUM: try adding symbols</li>
<li>U+241A SYMBOL FOR SUBSTITUTE: try adding symbols</li>
<li>U+241B SYMBOL FOR ESCAPE: try adding symbols</li>
<li>U+241C SYMBOL FOR FILE SEPARATOR: try adding symbols</li>
<li>U+241D SYMBOL FOR GROUP SEPARATOR: try adding symbols</li>
<li>U+241E SYMBOL FOR RECORD SEPARATOR: try adding symbols</li>
<li>U+241F SYMBOL FOR UNIT SEPARATOR: try adding symbols</li>
<li>U+2420 SYMBOL FOR SPACE: try adding symbols</li>
<li>U+2421 SYMBOL FOR DELETE: try adding symbols</li>
<li>U+2424 SYMBOL FOR NEWLINE: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25A7 SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL: try adding symbols</li>
<li>U+25A8 SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25AC BLACK RECTANGLE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BB WHITE RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C5 WHITE LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: cham, lepcha, chakma, bengali, newa, mongolian, yi, gunjala-gondi, miao, tifinagh, modi, limbu, osage, telugu, thai, tagbanwa, buginese, duployan, siddham, psalter-pahlavi, manichaean, armenian, caucasian-albanian, sogdian, bassa-vah, elbasan, lao, warang-citi, saurashtra, pahawh-hmong, tamil, kayah-li, grantha, mahajani, rejang, syloti-nagri, syriac, adlam, wancho, tai-viet, hanifi-rohingya, tai-le, soyombo, nko, khmer, phags-pa, khojki, hanunoo, mende-kikakui, ahom, tai-tham, new-tai-lue, devanagari, buhid, tibetan, masaram-gondi, coptic, symbols, tagalog, thaana, gujarati, kannada, sharada, sinhala, marchen, canadian-aboriginal, oriya, javanese, kaithi, myanmar, old-permic, meetei-mayek, brahmi, gurmukhi, tirhuta, batak, takri, balinese, kharoshthi, malayalam, dogra, sundanese, math, zanabazar-square, bhaiksuki, music, mandaic, khudawadi, hebrew</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D8 INVERSE BULLET: try adding symbols</li>
<li>U+25D9 INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25E2 BLACK LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E3 BLACK LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E4 BLACK UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E5 BLACK UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2601 CLOUD: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2610 BALLOT BOX: try adding symbols</li>
<li>U+2611 BALLOT BOX WITH CHECK: try adding symbols</li>
<li>U+2612 BALLOT BOX WITH X: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2639 WHITE FROWNING FACE: try adding symbols</li>
<li>U+263A WHITE SMILING FACE: try adding symbols</li>
<li>U+263B BLACK SMILING FACE: try adding symbols</li>
<li>U+263C WHITE SUN WITH RAYS: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2660 BLACK SPADE SUIT: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2663 BLACK CLUB SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2666 BLACK DIAMOND SUIT: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+2690 WHITE FLAG: try adding symbols</li>
<li>U+2691 BLACK FLAG: try adding symbols</li>
<li>U+26ED GEAR WITHOUT HUB: try adding symbols</li>
<li>U+2709 ENVELOPE: try adding symbols</li>
<li>U+270E LOWER RIGHT PENCIL: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2714 HEAVY CHECK MARK: try adding symbols</li>
<li>U+2715 MULTIPLICATION X: try adding symbols</li>
<li>U+2716 HEAVY MULTIPLICATION X: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2718 HEAVY BALLOT X: try adding symbols</li>
<li>U+271A HEAVY GREEK CROSS: try adding symbols</li>
<li>U+276E HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+276F HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+27C2 PERPENDICULAR: try adding math</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+2800 BRAILLE PATTERN BLANK: try adding one of: braille, symbols</li>
<li>U+2801 BRAILLE PATTERN DOTS-1: try adding one of: braille, symbols</li>
<li>U+2802 BRAILLE PATTERN DOTS-2: try adding one of: braille, symbols</li>
<li>U+2803 BRAILLE PATTERN DOTS-12: try adding one of: braille, symbols</li>
<li>U+2804 BRAILLE PATTERN DOTS-3: try adding one of: braille, symbols</li>
<li>U+2805 BRAILLE PATTERN DOTS-13: try adding one of: braille, symbols</li>
<li>U+2806 BRAILLE PATTERN DOTS-23: try adding one of: braille, symbols</li>
<li>U+2807 BRAILLE PATTERN DOTS-123: try adding one of: braille, symbols</li>
<li>U+2808 BRAILLE PATTERN DOTS-4: try adding one of: braille, symbols</li>
<li>U+2809 BRAILLE PATTERN DOTS-14: try adding one of: braille, symbols</li>
<li>U+280A BRAILLE PATTERN DOTS-24: try adding one of: braille, symbols</li>
<li>U+280B BRAILLE PATTERN DOTS-124: try adding one of: braille, symbols</li>
<li>U+280C BRAILLE PATTERN DOTS-34: try adding one of: braille, symbols</li>
<li>U+280D BRAILLE PATTERN DOTS-134: try adding one of: braille, symbols</li>
<li>U+280E BRAILLE PATTERN DOTS-234: try adding one of: braille, symbols</li>
<li>U+280F BRAILLE PATTERN DOTS-1234: try adding one of: braille, symbols</li>
<li>U+2810 BRAILLE PATTERN DOTS-5: try adding one of: braille, symbols</li>
<li>U+2811 BRAILLE PATTERN DOTS-15: try adding one of: braille, symbols</li>
<li>U+2812 BRAILLE PATTERN DOTS-25: try adding one of: braille, symbols</li>
<li>U+2813 BRAILLE PATTERN DOTS-125: try adding one of: braille, symbols</li>
<li>U+2814 BRAILLE PATTERN DOTS-35: try adding one of: braille, symbols</li>
<li>U+2815 BRAILLE PATTERN DOTS-135: try adding one of: braille, symbols</li>
<li>U+2816 BRAILLE PATTERN DOTS-235: try adding one of: braille, symbols</li>
<li>U+2817 BRAILLE PATTERN DOTS-1235: try adding one of: braille, symbols</li>
<li>U+2818 BRAILLE PATTERN DOTS-45: try adding one of: braille, symbols</li>
<li>U+2819 BRAILLE PATTERN DOTS-145: try adding one of: braille, symbols</li>
<li>U+281A BRAILLE PATTERN DOTS-245: try adding one of: braille, symbols</li>
<li>U+281B BRAILLE PATTERN DOTS-1245: try adding one of: braille, symbols</li>
<li>U+281C BRAILLE PATTERN DOTS-345: try adding one of: braille, symbols</li>
<li>U+281D BRAILLE PATTERN DOTS-1345: try adding one of: braille, symbols</li>
<li>U+281E BRAILLE PATTERN DOTS-2345: try adding one of: braille, symbols</li>
<li>U+281F BRAILLE PATTERN DOTS-12345: try adding one of: braille, symbols</li>
<li>U+2820 BRAILLE PATTERN DOTS-6: try adding one of: braille, symbols</li>
<li>U+2821 BRAILLE PATTERN DOTS-16: try adding one of: braille, symbols</li>
<li>U+2822 BRAILLE PATTERN DOTS-26: try adding one of: braille, symbols</li>
<li>U+2823 BRAILLE PATTERN DOTS-126: try adding one of: braille, symbols</li>
<li>U+2824 BRAILLE PATTERN DOTS-36: try adding one of: braille, symbols</li>
<li>U+2825 BRAILLE PATTERN DOTS-136: try adding one of: braille, symbols</li>
<li>U+2826 BRAILLE PATTERN DOTS-236: try adding one of: braille, symbols</li>
<li>U+2827 BRAILLE PATTERN DOTS-1236: try adding one of: braille, symbols</li>
<li>U+2828 BRAILLE PATTERN DOTS-46: try adding one of: braille, symbols</li>
<li>U+2829 BRAILLE PATTERN DOTS-146: try adding one of: braille, symbols</li>
<li>U+282A BRAILLE PATTERN DOTS-246: try adding one of: braille, symbols</li>
<li>U+282B BRAILLE PATTERN DOTS-1246: try adding one of: braille, symbols</li>
<li>U+282C BRAILLE PATTERN DOTS-346: try adding one of: braille, symbols</li>
<li>U+282D BRAILLE PATTERN DOTS-1346: try adding one of: braille, symbols</li>
<li>U+282E BRAILLE PATTERN DOTS-2346: try adding one of: braille, symbols</li>
<li>U+282F BRAILLE PATTERN DOTS-12346: try adding one of: braille, symbols</li>
<li>U+2830 BRAILLE PATTERN DOTS-56: try adding one of: braille, symbols</li>
<li>U+2831 BRAILLE PATTERN DOTS-156: try adding one of: braille, symbols</li>
<li>U+2832 BRAILLE PATTERN DOTS-256: try adding one of: braille, symbols</li>
<li>U+2833 BRAILLE PATTERN DOTS-1256: try adding one of: braille, symbols</li>
<li>U+2834 BRAILLE PATTERN DOTS-356: try adding one of: braille, symbols</li>
<li>U+2835 BRAILLE PATTERN DOTS-1356: try adding one of: braille, symbols</li>
<li>U+2836 BRAILLE PATTERN DOTS-2356: try adding one of: braille, symbols</li>
<li>U+2837 BRAILLE PATTERN DOTS-12356: try adding one of: braille, symbols</li>
<li>U+2838 BRAILLE PATTERN DOTS-456: try adding one of: braille, symbols</li>
<li>U+2839 BRAILLE PATTERN DOTS-1456: try adding one of: braille, symbols</li>
<li>U+283A BRAILLE PATTERN DOTS-2456: try adding one of: braille, symbols</li>
<li>U+283B BRAILLE PATTERN DOTS-12456: try adding one of: braille, symbols</li>
<li>U+283C BRAILLE PATTERN DOTS-3456: try adding one of: braille, symbols</li>
<li>U+283D BRAILLE PATTERN DOTS-13456: try adding one of: braille, symbols</li>
<li>U+283E BRAILLE PATTERN DOTS-23456: try adding one of: braille, symbols</li>
<li>U+283F BRAILLE PATTERN DOTS-123456: try adding one of: braille, symbols</li>
<li>U+2913 DOWNWARDS ARROW TO BAR: try adding math</li>
<li>U+2940 ANTICLOCKWISE CLOSED CIRCLE ARROW: try adding math</li>
<li>U+2B51 BLACK SMALL STAR: try adding symbols</li>
<li>U+2B52 WHITE SMALL STAR: try adding symbols</li>
<li>U+2BBD BALLOT BOX WITH LIGHT X: try adding symbols</li>
<li>U+2BE8 LEFT HALF BLACK STAR: try adding symbols</li>
<li>U+2BE9 RIGHT HALF BLACK STAR: try adding symbols</li>
<li>U+2BEA STAR WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+2BEB STAR WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+33D1 SQUARE LN: not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0A3 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+EC00 : not included in any glyphset definition</li>
<li>U+EC01 : not included in any glyphset definition</li>
<li>U+EC02 : not included in any glyphset definition</li>
<li>U+EC03 : not included in any glyphset definition</li>
<li>U+EC07 : not included in any glyphset definition</li>
<li>U+EC08 : not included in any glyphset definition</li>
<li>U+EC09 : not included in any glyphset definition</li>
<li>U+EC0A : not included in any glyphset definition</li>
<li>U+EC25 : not included in any glyphset definition</li>
<li>U+EC26 : not included in any glyphset definition</li>
<li>U+EC27 : not included in any glyphset definition</li>
<li>U+EC28 : not included in any glyphset definition</li>
<li>U+EC2A : not included in any glyphset definition</li>
<li>U+EC2B : not included in any glyphset definition</li>
<li>U+EC2C : not included in any glyphset definition</li>
<li>U+EC2E : not included in any glyphset definition</li>
<li>U+EC2F : not included in any glyphset definition</li>
<li>U+1F319 CRESCENT MOON: not included in any glyphset definition</li>
<li>U+1F327 CLOUD WITH RAIN: try adding symbols</li>
<li>U+1F3E0 HOUSE BUILDING: try adding symbols</li>
<li>U+1F44D THUMBS UP SIGN: try adding symbols</li>
<li>U+1F44E THUMBS DOWN SIGN: try adding symbols</li>
<li>U+1F464 BUST IN SILHOUETTE: not included in any glyphset definition</li>
<li>U+1F4AC SPEECH BALLOON: not included in any glyphset definition</li>
<li>U+1F4BE FLOPPY DISK: not included in any glyphset definition</li>
<li>U+1F4C0 DVD: not included in any glyphset definition</li>
<li>U+1F4C1 FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C2 OPEN FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C6 TEAR-OFF CALENDAR: not included in any glyphset definition</li>
<li>U+1F4DE TELEPHONE RECEIVER: not included in any glyphset definition</li>
<li>U+1F4F1 MOBILE PHONE: not included in any glyphset definition</li>
<li>U+1F4F6 ANTENNA WITH BARS: not included in any glyphset definition</li>
<li>U+1F500 TWISTED RIGHTWARDS ARROWS: not included in any glyphset definition</li>
<li>U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS: not included in any glyphset definition</li>
<li>U+1F508 SPEAKER: try adding symbols</li>
<li>U+1F50A SPEAKER WITH THREE SOUND WAVES: try adding symbols</li>
<li>U+1F50D LEFT-POINTING MAGNIFYING GLASS: try adding symbols</li>
<li>U+1F50E RIGHT-POINTING MAGNIFYING GLASS: not included in any glyphset definition</li>
<li>U+1F511 KEY: not included in any glyphset definition</li>
<li>U+1F512 LOCK: try adding symbols</li>
<li>U+1F513 OPEN LOCK: try adding symbols</li>
<li>U+1F5A4 BLACK HEART: try adding symbols</li>
<li>U+1F5C0 FOLDER: try adding symbols</li>
<li>U+1F5C1 OPEN FOLDER: try adding symbols</li>
<li>U+1F5D1 WASTEBASKET: try adding symbols</li>
<li>U+1F5D5 MINIMIZE: try adding symbols</li>
<li>U+1F5D6 MAXIMIZE: try adding symbols</li>
<li>U+1F5D8 CLOCKWISE RIGHT AND LEFT SEMICIRCLE ARROWS: try adding symbols</li>
<li>U+1F5F4 BALLOT SCRIPT X: try adding symbols</li>
<li>U+1F5F5 BALLOT BOX WITH SCRIPT X: try adding symbols</li>
<li>U+1F5F6 BALLOT BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F7 BALLOT BOX WITH BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F9 BALLOT BOX WITH BOLD CHECK: try adding symbols</li>
<li>U+1F600 GRINNING FACE: not included in any glyphset definition</li>
<li>U+1F601 GRINNING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F60A SMILING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F620 ANGRY FACE: not included in any glyphset definition</li>
<li>U+1F621 POUTING FACE: not included in any glyphset definition</li>
<li>U+1F6C9 BOYS SYMBOL: try adding symbols</li>
<li>U+1F6CA GIRLS SYMBOL: try adding symbols</li>
<li>U+1F6D2 SHOPPING TROLLEY: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[9] SudoUI-Italic[YTDE,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: e̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: E̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: é̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: É̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: è̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: È̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: o̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: O̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: s̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: S̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* 🔥 **FAIL** <p>The defaul value YTDE:-231.0 is not registered as an axis fallback name on the Google Axis Registry.
You should consider suggesting the addition of this value to the registry or adopted one of the existing fallback names for this axis:
[name: &quot;Normal&quot;
value: -250.0
]</p>
 [code: not-registered]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>Axis Value for 'YTDE':'Normal' is expected to be '-250.0' but this font has 'Normal'='-231.0'.</p>
 [code: bad-coordinate]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ⚠️ **WARN** <p>In order to optimize performance on some legacy renderers, the value of unitsPerEm at the head table should ideally be a power of 2 between 16 to 16384. And values of 1000 and 2000 are also common and may be just fine as well. But we got 832 instead.</p>
 [code: suboptimal]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>There is only one CJK glyph when there needs to be at least 150 in order to support the smallest CJK writing system, Kana.
The following CJK glyphs were found:
['uni33D1']
Please check that these glyphs have the correct unicodes.</p>
 [code: cjk-not-enough-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni0253 (U+0253): L&lt;&lt;190.0,512.0&gt;--&lt;118.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0257 (U+0257): L&lt;&lt;446.0,512.0&gt;--&lt;374.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0199 (U+0199): L&lt;&lt;190.0,512.0&gt;--&lt;118.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0272 (U+0272): L&lt;&lt;87.0,0.0&gt;--&lt;15.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01B4 (U+01B4): L&lt;&lt;363.0,448.0&gt;--&lt;435.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;120.0,35.0&gt;--&lt;176.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;220.0,35.0&gt;--&lt;276.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* uni019D (U+019D): L&lt;&lt;87.0,0.0&gt;--&lt;15.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, coptic, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, gothic, glagolitic, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, syriac, old-permic, tai-le, coptic, duployan, math, tifinagh, todhri, canadian-aboriginal, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: sunuwar, math</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, syriac, cherokee, tifinagh, sunuwar, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, hatran, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, old-hungarian, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A5 UPWARDS ARROW FROM BAR: try adding math</li>
<li>U+21A8 UP DOWN ARROW WITH BASE: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2204 THERE DOES NOT EXIST: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2216 SET MINUS: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, tai-tham, symbols, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+221F RIGHT ANGLE: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2236 RATIO: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2259 ESTIMATES: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+2302 HOUSE: try adding symbols</li>
<li>U+2310 REVERSED NOT SIGN: try adding math</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2320 TOP HALF INTEGRAL: try adding math</li>
<li>U+2321 BOTTOM HALF INTEGRAL: try adding math</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23ED BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23EE BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23F5 BLACK MEDIUM RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+2400 SYMBOL FOR NULL: try adding symbols</li>
<li>U+2401 SYMBOL FOR START OF HEADING: try adding symbols</li>
<li>U+2402 SYMBOL FOR START OF TEXT: try adding symbols</li>
<li>U+2403 SYMBOL FOR END OF TEXT: try adding symbols</li>
<li>U+2404 SYMBOL FOR END OF TRANSMISSION: try adding symbols</li>
<li>U+2405 SYMBOL FOR ENQUIRY: try adding symbols</li>
<li>U+2406 SYMBOL FOR ACKNOWLEDGE: try adding symbols</li>
<li>U+2407 SYMBOL FOR BELL: try adding symbols</li>
<li>U+2408 SYMBOL FOR BACKSPACE: try adding symbols</li>
<li>U+2409 SYMBOL FOR HORIZONTAL TABULATION: try adding symbols</li>
<li>U+240A SYMBOL FOR LINE FEED: try adding symbols</li>
<li>U+240B SYMBOL FOR VERTICAL TABULATION: try adding symbols</li>
<li>U+240C SYMBOL FOR FORM FEED: try adding symbols</li>
<li>U+240D SYMBOL FOR CARRIAGE RETURN: try adding symbols</li>
<li>U+240E SYMBOL FOR SHIFT OUT: try adding symbols</li>
<li>U+240F SYMBOL FOR SHIFT IN: try adding symbols</li>
<li>U+2410 SYMBOL FOR DATA LINK ESCAPE: try adding symbols</li>
<li>U+2411 SYMBOL FOR DEVICE CONTROL ONE: try adding symbols</li>
<li>U+2412 SYMBOL FOR DEVICE CONTROL TWO: try adding symbols</li>
<li>U+2413 SYMBOL FOR DEVICE CONTROL THREE: try adding symbols</li>
<li>U+2414 SYMBOL FOR DEVICE CONTROL FOUR: try adding symbols</li>
<li>U+2415 SYMBOL FOR NEGATIVE ACKNOWLEDGE: try adding symbols</li>
<li>U+2416 SYMBOL FOR SYNCHRONOUS IDLE: try adding symbols</li>
<li>U+2417 SYMBOL FOR END OF TRANSMISSION BLOCK: try adding symbols</li>
<li>U+2418 SYMBOL FOR CANCEL: try adding symbols</li>
<li>U+2419 SYMBOL FOR END OF MEDIUM: try adding symbols</li>
<li>U+241A SYMBOL FOR SUBSTITUTE: try adding symbols</li>
<li>U+241B SYMBOL FOR ESCAPE: try adding symbols</li>
<li>U+241C SYMBOL FOR FILE SEPARATOR: try adding symbols</li>
<li>U+241D SYMBOL FOR GROUP SEPARATOR: try adding symbols</li>
<li>U+241E SYMBOL FOR RECORD SEPARATOR: try adding symbols</li>
<li>U+241F SYMBOL FOR UNIT SEPARATOR: try adding symbols</li>
<li>U+2420 SYMBOL FOR SPACE: try adding symbols</li>
<li>U+2421 SYMBOL FOR DELETE: try adding symbols</li>
<li>U+2424 SYMBOL FOR NEWLINE: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25A7 SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL: try adding symbols</li>
<li>U+25A8 SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25AC BLACK RECTANGLE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BB WHITE RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C5 WHITE LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: cham, lepcha, chakma, bengali, newa, mongolian, yi, gunjala-gondi, miao, tifinagh, modi, limbu, osage, telugu, thai, tagbanwa, buginese, duployan, siddham, psalter-pahlavi, manichaean, armenian, caucasian-albanian, sogdian, bassa-vah, elbasan, lao, warang-citi, saurashtra, pahawh-hmong, tamil, kayah-li, grantha, mahajani, rejang, syloti-nagri, syriac, adlam, wancho, tai-viet, hanifi-rohingya, tai-le, soyombo, nko, khmer, phags-pa, khojki, hanunoo, mende-kikakui, ahom, tai-tham, new-tai-lue, devanagari, buhid, tibetan, masaram-gondi, coptic, symbols, tagalog, thaana, gujarati, kannada, sharada, sinhala, marchen, canadian-aboriginal, oriya, javanese, kaithi, myanmar, old-permic, meetei-mayek, brahmi, gurmukhi, tirhuta, batak, takri, balinese, kharoshthi, malayalam, dogra, sundanese, math, zanabazar-square, bhaiksuki, music, mandaic, khudawadi, hebrew</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D8 INVERSE BULLET: try adding symbols</li>
<li>U+25D9 INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25E2 BLACK LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E3 BLACK LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E4 BLACK UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E5 BLACK UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2601 CLOUD: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2610 BALLOT BOX: try adding symbols</li>
<li>U+2611 BALLOT BOX WITH CHECK: try adding symbols</li>
<li>U+2612 BALLOT BOX WITH X: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2639 WHITE FROWNING FACE: try adding symbols</li>
<li>U+263A WHITE SMILING FACE: try adding symbols</li>
<li>U+263B BLACK SMILING FACE: try adding symbols</li>
<li>U+263C WHITE SUN WITH RAYS: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2660 BLACK SPADE SUIT: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2663 BLACK CLUB SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2666 BLACK DIAMOND SUIT: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+2690 WHITE FLAG: try adding symbols</li>
<li>U+2691 BLACK FLAG: try adding symbols</li>
<li>U+26ED GEAR WITHOUT HUB: try adding symbols</li>
<li>U+2709 ENVELOPE: try adding symbols</li>
<li>U+270E LOWER RIGHT PENCIL: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2714 HEAVY CHECK MARK: try adding symbols</li>
<li>U+2715 MULTIPLICATION X: try adding symbols</li>
<li>U+2716 HEAVY MULTIPLICATION X: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2718 HEAVY BALLOT X: try adding symbols</li>
<li>U+271A HEAVY GREEK CROSS: try adding symbols</li>
<li>U+276E HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+276F HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+27C2 PERPENDICULAR: try adding math</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+2800 BRAILLE PATTERN BLANK: try adding one of: braille, symbols</li>
<li>U+2801 BRAILLE PATTERN DOTS-1: try adding one of: braille, symbols</li>
<li>U+2802 BRAILLE PATTERN DOTS-2: try adding one of: braille, symbols</li>
<li>U+2803 BRAILLE PATTERN DOTS-12: try adding one of: braille, symbols</li>
<li>U+2804 BRAILLE PATTERN DOTS-3: try adding one of: braille, symbols</li>
<li>U+2805 BRAILLE PATTERN DOTS-13: try adding one of: braille, symbols</li>
<li>U+2806 BRAILLE PATTERN DOTS-23: try adding one of: braille, symbols</li>
<li>U+2807 BRAILLE PATTERN DOTS-123: try adding one of: braille, symbols</li>
<li>U+2808 BRAILLE PATTERN DOTS-4: try adding one of: braille, symbols</li>
<li>U+2809 BRAILLE PATTERN DOTS-14: try adding one of: braille, symbols</li>
<li>U+280A BRAILLE PATTERN DOTS-24: try adding one of: braille, symbols</li>
<li>U+280B BRAILLE PATTERN DOTS-124: try adding one of: braille, symbols</li>
<li>U+280C BRAILLE PATTERN DOTS-34: try adding one of: braille, symbols</li>
<li>U+280D BRAILLE PATTERN DOTS-134: try adding one of: braille, symbols</li>
<li>U+280E BRAILLE PATTERN DOTS-234: try adding one of: braille, symbols</li>
<li>U+280F BRAILLE PATTERN DOTS-1234: try adding one of: braille, symbols</li>
<li>U+2810 BRAILLE PATTERN DOTS-5: try adding one of: braille, symbols</li>
<li>U+2811 BRAILLE PATTERN DOTS-15: try adding one of: braille, symbols</li>
<li>U+2812 BRAILLE PATTERN DOTS-25: try adding one of: braille, symbols</li>
<li>U+2813 BRAILLE PATTERN DOTS-125: try adding one of: braille, symbols</li>
<li>U+2814 BRAILLE PATTERN DOTS-35: try adding one of: braille, symbols</li>
<li>U+2815 BRAILLE PATTERN DOTS-135: try adding one of: braille, symbols</li>
<li>U+2816 BRAILLE PATTERN DOTS-235: try adding one of: braille, symbols</li>
<li>U+2817 BRAILLE PATTERN DOTS-1235: try adding one of: braille, symbols</li>
<li>U+2818 BRAILLE PATTERN DOTS-45: try adding one of: braille, symbols</li>
<li>U+2819 BRAILLE PATTERN DOTS-145: try adding one of: braille, symbols</li>
<li>U+281A BRAILLE PATTERN DOTS-245: try adding one of: braille, symbols</li>
<li>U+281B BRAILLE PATTERN DOTS-1245: try adding one of: braille, symbols</li>
<li>U+281C BRAILLE PATTERN DOTS-345: try adding one of: braille, symbols</li>
<li>U+281D BRAILLE PATTERN DOTS-1345: try adding one of: braille, symbols</li>
<li>U+281E BRAILLE PATTERN DOTS-2345: try adding one of: braille, symbols</li>
<li>U+281F BRAILLE PATTERN DOTS-12345: try adding one of: braille, symbols</li>
<li>U+2820 BRAILLE PATTERN DOTS-6: try adding one of: braille, symbols</li>
<li>U+2821 BRAILLE PATTERN DOTS-16: try adding one of: braille, symbols</li>
<li>U+2822 BRAILLE PATTERN DOTS-26: try adding one of: braille, symbols</li>
<li>U+2823 BRAILLE PATTERN DOTS-126: try adding one of: braille, symbols</li>
<li>U+2824 BRAILLE PATTERN DOTS-36: try adding one of: braille, symbols</li>
<li>U+2825 BRAILLE PATTERN DOTS-136: try adding one of: braille, symbols</li>
<li>U+2826 BRAILLE PATTERN DOTS-236: try adding one of: braille, symbols</li>
<li>U+2827 BRAILLE PATTERN DOTS-1236: try adding one of: braille, symbols</li>
<li>U+2828 BRAILLE PATTERN DOTS-46: try adding one of: braille, symbols</li>
<li>U+2829 BRAILLE PATTERN DOTS-146: try adding one of: braille, symbols</li>
<li>U+282A BRAILLE PATTERN DOTS-246: try adding one of: braille, symbols</li>
<li>U+282B BRAILLE PATTERN DOTS-1246: try adding one of: braille, symbols</li>
<li>U+282C BRAILLE PATTERN DOTS-346: try adding one of: braille, symbols</li>
<li>U+282D BRAILLE PATTERN DOTS-1346: try adding one of: braille, symbols</li>
<li>U+282E BRAILLE PATTERN DOTS-2346: try adding one of: braille, symbols</li>
<li>U+282F BRAILLE PATTERN DOTS-12346: try adding one of: braille, symbols</li>
<li>U+2830 BRAILLE PATTERN DOTS-56: try adding one of: braille, symbols</li>
<li>U+2831 BRAILLE PATTERN DOTS-156: try adding one of: braille, symbols</li>
<li>U+2832 BRAILLE PATTERN DOTS-256: try adding one of: braille, symbols</li>
<li>U+2833 BRAILLE PATTERN DOTS-1256: try adding one of: braille, symbols</li>
<li>U+2834 BRAILLE PATTERN DOTS-356: try adding one of: braille, symbols</li>
<li>U+2835 BRAILLE PATTERN DOTS-1356: try adding one of: braille, symbols</li>
<li>U+2836 BRAILLE PATTERN DOTS-2356: try adding one of: braille, symbols</li>
<li>U+2837 BRAILLE PATTERN DOTS-12356: try adding one of: braille, symbols</li>
<li>U+2838 BRAILLE PATTERN DOTS-456: try adding one of: braille, symbols</li>
<li>U+2839 BRAILLE PATTERN DOTS-1456: try adding one of: braille, symbols</li>
<li>U+283A BRAILLE PATTERN DOTS-2456: try adding one of: braille, symbols</li>
<li>U+283B BRAILLE PATTERN DOTS-12456: try adding one of: braille, symbols</li>
<li>U+283C BRAILLE PATTERN DOTS-3456: try adding one of: braille, symbols</li>
<li>U+283D BRAILLE PATTERN DOTS-13456: try adding one of: braille, symbols</li>
<li>U+283E BRAILLE PATTERN DOTS-23456: try adding one of: braille, symbols</li>
<li>U+283F BRAILLE PATTERN DOTS-123456: try adding one of: braille, symbols</li>
<li>U+2913 DOWNWARDS ARROW TO BAR: try adding math</li>
<li>U+2940 ANTICLOCKWISE CLOSED CIRCLE ARROW: try adding math</li>
<li>U+2B51 BLACK SMALL STAR: try adding symbols</li>
<li>U+2B52 WHITE SMALL STAR: try adding symbols</li>
<li>U+2BBD BALLOT BOX WITH LIGHT X: try adding symbols</li>
<li>U+2BE8 LEFT HALF BLACK STAR: try adding symbols</li>
<li>U+2BE9 RIGHT HALF BLACK STAR: try adding symbols</li>
<li>U+2BEA STAR WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+2BEB STAR WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+33D1 SQUARE LN: not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0A3 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+EC00 : not included in any glyphset definition</li>
<li>U+EC01 : not included in any glyphset definition</li>
<li>U+EC02 : not included in any glyphset definition</li>
<li>U+EC03 : not included in any glyphset definition</li>
<li>U+EC07 : not included in any glyphset definition</li>
<li>U+EC08 : not included in any glyphset definition</li>
<li>U+EC09 : not included in any glyphset definition</li>
<li>U+EC0A : not included in any glyphset definition</li>
<li>U+EC25 : not included in any glyphset definition</li>
<li>U+EC26 : not included in any glyphset definition</li>
<li>U+EC27 : not included in any glyphset definition</li>
<li>U+EC28 : not included in any glyphset definition</li>
<li>U+EC2A : not included in any glyphset definition</li>
<li>U+EC2B : not included in any glyphset definition</li>
<li>U+EC2C : not included in any glyphset definition</li>
<li>U+EC2E : not included in any glyphset definition</li>
<li>U+EC2F : not included in any glyphset definition</li>
<li>U+1F319 CRESCENT MOON: not included in any glyphset definition</li>
<li>U+1F327 CLOUD WITH RAIN: try adding symbols</li>
<li>U+1F3E0 HOUSE BUILDING: try adding symbols</li>
<li>U+1F44D THUMBS UP SIGN: try adding symbols</li>
<li>U+1F44E THUMBS DOWN SIGN: try adding symbols</li>
<li>U+1F464 BUST IN SILHOUETTE: not included in any glyphset definition</li>
<li>U+1F4AC SPEECH BALLOON: not included in any glyphset definition</li>
<li>U+1F4BE FLOPPY DISK: not included in any glyphset definition</li>
<li>U+1F4C0 DVD: not included in any glyphset definition</li>
<li>U+1F4C1 FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C2 OPEN FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C6 TEAR-OFF CALENDAR: not included in any glyphset definition</li>
<li>U+1F4DE TELEPHONE RECEIVER: not included in any glyphset definition</li>
<li>U+1F4F1 MOBILE PHONE: not included in any glyphset definition</li>
<li>U+1F4F6 ANTENNA WITH BARS: not included in any glyphset definition</li>
<li>U+1F500 TWISTED RIGHTWARDS ARROWS: not included in any glyphset definition</li>
<li>U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS: not included in any glyphset definition</li>
<li>U+1F508 SPEAKER: try adding symbols</li>
<li>U+1F50A SPEAKER WITH THREE SOUND WAVES: try adding symbols</li>
<li>U+1F50D LEFT-POINTING MAGNIFYING GLASS: try adding symbols</li>
<li>U+1F50E RIGHT-POINTING MAGNIFYING GLASS: not included in any glyphset definition</li>
<li>U+1F511 KEY: not included in any glyphset definition</li>
<li>U+1F512 LOCK: try adding symbols</li>
<li>U+1F513 OPEN LOCK: try adding symbols</li>
<li>U+1F5A4 BLACK HEART: try adding symbols</li>
<li>U+1F5C0 FOLDER: try adding symbols</li>
<li>U+1F5C1 OPEN FOLDER: try adding symbols</li>
<li>U+1F5D1 WASTEBASKET: try adding symbols</li>
<li>U+1F5D5 MINIMIZE: try adding symbols</li>
<li>U+1F5D6 MAXIMIZE: try adding symbols</li>
<li>U+1F5D8 CLOCKWISE RIGHT AND LEFT SEMICIRCLE ARROWS: try adding symbols</li>
<li>U+1F5F4 BALLOT SCRIPT X: try adding symbols</li>
<li>U+1F5F5 BALLOT BOX WITH SCRIPT X: try adding symbols</li>
<li>U+1F5F6 BALLOT BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F7 BALLOT BOX WITH BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F9 BALLOT BOX WITH BOLD CHECK: try adding symbols</li>
<li>U+1F600 GRINNING FACE: not included in any glyphset definition</li>
<li>U+1F601 GRINNING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F60A SMILING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F620 ANGRY FACE: not included in any glyphset definition</li>
<li>U+1F621 POUTING FACE: not included in any glyphset definition</li>
<li>U+1F6C9 BOYS SYMBOL: try adding symbols</li>
<li>U+1F6CA GIRLS SYMBOL: try adding symbols</li>
<li>U+1F6D2 SHOPPING TROLLEY: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[9] SudoUI[YTDE,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: e̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: E̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: é̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: É̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: è̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: È̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: o̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: O̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: s̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: S̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* 🔥 **FAIL** <p>The defaul value YTDE:-231.0 is not registered as an axis fallback name on the Google Axis Registry.
You should consider suggesting the addition of this value to the registry or adopted one of the existing fallback names for this axis:
[name: &quot;Normal&quot;
value: -250.0
]</p>
 [code: not-registered]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>Axis Value for 'YTDE':'Normal' is expected to be '-250.0' but this font has 'Normal'='-231.0'.</p>
 [code: bad-coordinate]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ⚠️ **WARN** <p>In order to optimize performance on some legacy renderers, the value of unitsPerEm at the head table should ideally be a power of 2 between 16 to 16384. And values of 1000 and 2000 are also common and may be just fine as well. But we got 832 instead.</p>
 [code: suboptimal]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>There is only one CJK glyph when there needs to be at least 150 in order to support the smallest CJK writing system, Kana.
The following CJK glyphs were found:
['uni33D1']
Please check that these glyphs have the correct unicodes.</p>
 [code: cjk-not-enough-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni0253 (U+0253): L&lt;&lt;132.0,512.0&gt;--&lt;60.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0257 (U+0257): L&lt;&lt;388.0,512.0&gt;--&lt;316.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0199 (U+0199): L&lt;&lt;132.0,512.0&gt;--&lt;60.0,512.0&gt;&gt; has the same coordinates as a previous segment.

* uni0272 (U+0272): L&lt;&lt;132.0,0.0&gt;--&lt;60.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01B4 (U+01B4): L&lt;&lt;318.0,448.0&gt;--&lt;390.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;158.0,35.0&gt;--&lt;214.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* colonmonetary (U+20A1): L&lt;&lt;258.0,35.0&gt;--&lt;314.0,35.0&gt;&gt; has the same coordinates as a previous segment.

* uni019D (U+019D): L&lt;&lt;132.0,0.0&gt;--&lt;60.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, coptic, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, gothic, glagolitic, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, syriac, old-permic, tai-le, coptic, duployan, math, tifinagh, todhri, canadian-aboriginal, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: sunuwar, math</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, syriac, cherokee, tifinagh, sunuwar, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+200C ZERO WIDTH NON-JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, hatran, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+200D ZERO WIDTH JOINER: try adding one of: khmer, phags-pa, lao, cham, lepcha, khojki, meetei-mayek, chakma, bengali, hanunoo, newa, mongolian, tai-tham, new-tai-lue, warang-citi, khudawadi, arabic, brahmi, devanagari, old-hungarian, saurashtra, buhid, gunjala-gondi, gurmukhi, pahawh-hmong, tamil, yi, tifinagh, modi, tirhuta, limbu, kayah-li, batak, grantha, takri, balinese, telugu, kharoshthi, mahajani, thai, tagbanwa, rejang, malayalam, syloti-nagri, syriac, buginese, dogra, masaram-gondi, tibetan, sundanese, duployan, siddham, psalter-pahlavi, manichaean, zanabazar-square, bhaiksuki, tagalog, thaana, gujarati, mandaic, kannada, tai-viet, hanifi-rohingya, sharada, tai-le, sogdian, sinhala, nko, oriya, javanese, kaithi, myanmar, avestan, hebrew</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A5 UPWARDS ARROW FROM BAR: try adding math</li>
<li>U+21A8 UP DOWN ARROW WITH BASE: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2204 THERE DOES NOT EXIST: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2216 SET MINUS: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, tai-tham, symbols, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+221F RIGHT ANGLE: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2236 RATIO: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2259 ESTIMATES: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+2302 HOUSE: try adding symbols</li>
<li>U+2310 REVERSED NOT SIGN: try adding math</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2320 TOP HALF INTEGRAL: try adding math</li>
<li>U+2321 BOTTOM HALF INTEGRAL: try adding math</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23ED BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23EE BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR: try adding symbols</li>
<li>U+23F5 BLACK MEDIUM RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+2400 SYMBOL FOR NULL: try adding symbols</li>
<li>U+2401 SYMBOL FOR START OF HEADING: try adding symbols</li>
<li>U+2402 SYMBOL FOR START OF TEXT: try adding symbols</li>
<li>U+2403 SYMBOL FOR END OF TEXT: try adding symbols</li>
<li>U+2404 SYMBOL FOR END OF TRANSMISSION: try adding symbols</li>
<li>U+2405 SYMBOL FOR ENQUIRY: try adding symbols</li>
<li>U+2406 SYMBOL FOR ACKNOWLEDGE: try adding symbols</li>
<li>U+2407 SYMBOL FOR BELL: try adding symbols</li>
<li>U+2408 SYMBOL FOR BACKSPACE: try adding symbols</li>
<li>U+2409 SYMBOL FOR HORIZONTAL TABULATION: try adding symbols</li>
<li>U+240A SYMBOL FOR LINE FEED: try adding symbols</li>
<li>U+240B SYMBOL FOR VERTICAL TABULATION: try adding symbols</li>
<li>U+240C SYMBOL FOR FORM FEED: try adding symbols</li>
<li>U+240D SYMBOL FOR CARRIAGE RETURN: try adding symbols</li>
<li>U+240E SYMBOL FOR SHIFT OUT: try adding symbols</li>
<li>U+240F SYMBOL FOR SHIFT IN: try adding symbols</li>
<li>U+2410 SYMBOL FOR DATA LINK ESCAPE: try adding symbols</li>
<li>U+2411 SYMBOL FOR DEVICE CONTROL ONE: try adding symbols</li>
<li>U+2412 SYMBOL FOR DEVICE CONTROL TWO: try adding symbols</li>
<li>U+2413 SYMBOL FOR DEVICE CONTROL THREE: try adding symbols</li>
<li>U+2414 SYMBOL FOR DEVICE CONTROL FOUR: try adding symbols</li>
<li>U+2415 SYMBOL FOR NEGATIVE ACKNOWLEDGE: try adding symbols</li>
<li>U+2416 SYMBOL FOR SYNCHRONOUS IDLE: try adding symbols</li>
<li>U+2417 SYMBOL FOR END OF TRANSMISSION BLOCK: try adding symbols</li>
<li>U+2418 SYMBOL FOR CANCEL: try adding symbols</li>
<li>U+2419 SYMBOL FOR END OF MEDIUM: try adding symbols</li>
<li>U+241A SYMBOL FOR SUBSTITUTE: try adding symbols</li>
<li>U+241B SYMBOL FOR ESCAPE: try adding symbols</li>
<li>U+241C SYMBOL FOR FILE SEPARATOR: try adding symbols</li>
<li>U+241D SYMBOL FOR GROUP SEPARATOR: try adding symbols</li>
<li>U+241E SYMBOL FOR RECORD SEPARATOR: try adding symbols</li>
<li>U+241F SYMBOL FOR UNIT SEPARATOR: try adding symbols</li>
<li>U+2420 SYMBOL FOR SPACE: try adding symbols</li>
<li>U+2421 SYMBOL FOR DELETE: try adding symbols</li>
<li>U+2424 SYMBOL FOR NEWLINE: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25A7 SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL: try adding symbols</li>
<li>U+25A8 SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25AC BLACK RECTANGLE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BB WHITE RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C5 WHITE LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: cham, lepcha, chakma, bengali, newa, mongolian, yi, gunjala-gondi, miao, tifinagh, modi, limbu, osage, telugu, thai, tagbanwa, buginese, duployan, siddham, psalter-pahlavi, manichaean, armenian, caucasian-albanian, sogdian, bassa-vah, elbasan, lao, warang-citi, saurashtra, pahawh-hmong, tamil, kayah-li, grantha, mahajani, rejang, syloti-nagri, syriac, adlam, wancho, tai-viet, hanifi-rohingya, tai-le, soyombo, nko, khmer, phags-pa, khojki, hanunoo, mende-kikakui, ahom, tai-tham, new-tai-lue, devanagari, buhid, tibetan, masaram-gondi, coptic, symbols, tagalog, thaana, gujarati, kannada, sharada, sinhala, marchen, canadian-aboriginal, oriya, javanese, kaithi, myanmar, old-permic, meetei-mayek, brahmi, gurmukhi, tirhuta, batak, takri, balinese, kharoshthi, malayalam, dogra, sundanese, math, zanabazar-square, bhaiksuki, music, mandaic, khudawadi, hebrew</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D8 INVERSE BULLET: try adding symbols</li>
<li>U+25D9 INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25E2 BLACK LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E3 BLACK LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E4 BLACK UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E5 BLACK UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2601 CLOUD: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2610 BALLOT BOX: try adding symbols</li>
<li>U+2611 BALLOT BOX WITH CHECK: try adding symbols</li>
<li>U+2612 BALLOT BOX WITH X: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2639 WHITE FROWNING FACE: try adding symbols</li>
<li>U+263A WHITE SMILING FACE: try adding symbols</li>
<li>U+263B BLACK SMILING FACE: try adding symbols</li>
<li>U+263C WHITE SUN WITH RAYS: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2660 BLACK SPADE SUIT: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2663 BLACK CLUB SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2666 BLACK DIAMOND SUIT: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+2690 WHITE FLAG: try adding symbols</li>
<li>U+2691 BLACK FLAG: try adding symbols</li>
<li>U+26ED GEAR WITHOUT HUB: try adding symbols</li>
<li>U+2709 ENVELOPE: try adding symbols</li>
<li>U+270E LOWER RIGHT PENCIL: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2714 HEAVY CHECK MARK: try adding symbols</li>
<li>U+2715 MULTIPLICATION X: try adding symbols</li>
<li>U+2716 HEAVY MULTIPLICATION X: try adding symbols</li>
<li>U+2717 BALLOT X: try adding symbols</li>
<li>U+2718 HEAVY BALLOT X: try adding symbols</li>
<li>U+271A HEAVY GREEK CROSS: try adding symbols</li>
<li>U+276E HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+276F HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT: try adding symbols</li>
<li>U+27C2 PERPENDICULAR: try adding math</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+2800 BRAILLE PATTERN BLANK: try adding one of: braille, symbols</li>
<li>U+2801 BRAILLE PATTERN DOTS-1: try adding one of: braille, symbols</li>
<li>U+2802 BRAILLE PATTERN DOTS-2: try adding one of: braille, symbols</li>
<li>U+2803 BRAILLE PATTERN DOTS-12: try adding one of: braille, symbols</li>
<li>U+2804 BRAILLE PATTERN DOTS-3: try adding one of: braille, symbols</li>
<li>U+2805 BRAILLE PATTERN DOTS-13: try adding one of: braille, symbols</li>
<li>U+2806 BRAILLE PATTERN DOTS-23: try adding one of: braille, symbols</li>
<li>U+2807 BRAILLE PATTERN DOTS-123: try adding one of: braille, symbols</li>
<li>U+2808 BRAILLE PATTERN DOTS-4: try adding one of: braille, symbols</li>
<li>U+2809 BRAILLE PATTERN DOTS-14: try adding one of: braille, symbols</li>
<li>U+280A BRAILLE PATTERN DOTS-24: try adding one of: braille, symbols</li>
<li>U+280B BRAILLE PATTERN DOTS-124: try adding one of: braille, symbols</li>
<li>U+280C BRAILLE PATTERN DOTS-34: try adding one of: braille, symbols</li>
<li>U+280D BRAILLE PATTERN DOTS-134: try adding one of: braille, symbols</li>
<li>U+280E BRAILLE PATTERN DOTS-234: try adding one of: braille, symbols</li>
<li>U+280F BRAILLE PATTERN DOTS-1234: try adding one of: braille, symbols</li>
<li>U+2810 BRAILLE PATTERN DOTS-5: try adding one of: braille, symbols</li>
<li>U+2811 BRAILLE PATTERN DOTS-15: try adding one of: braille, symbols</li>
<li>U+2812 BRAILLE PATTERN DOTS-25: try adding one of: braille, symbols</li>
<li>U+2813 BRAILLE PATTERN DOTS-125: try adding one of: braille, symbols</li>
<li>U+2814 BRAILLE PATTERN DOTS-35: try adding one of: braille, symbols</li>
<li>U+2815 BRAILLE PATTERN DOTS-135: try adding one of: braille, symbols</li>
<li>U+2816 BRAILLE PATTERN DOTS-235: try adding one of: braille, symbols</li>
<li>U+2817 BRAILLE PATTERN DOTS-1235: try adding one of: braille, symbols</li>
<li>U+2818 BRAILLE PATTERN DOTS-45: try adding one of: braille, symbols</li>
<li>U+2819 BRAILLE PATTERN DOTS-145: try adding one of: braille, symbols</li>
<li>U+281A BRAILLE PATTERN DOTS-245: try adding one of: braille, symbols</li>
<li>U+281B BRAILLE PATTERN DOTS-1245: try adding one of: braille, symbols</li>
<li>U+281C BRAILLE PATTERN DOTS-345: try adding one of: braille, symbols</li>
<li>U+281D BRAILLE PATTERN DOTS-1345: try adding one of: braille, symbols</li>
<li>U+281E BRAILLE PATTERN DOTS-2345: try adding one of: braille, symbols</li>
<li>U+281F BRAILLE PATTERN DOTS-12345: try adding one of: braille, symbols</li>
<li>U+2820 BRAILLE PATTERN DOTS-6: try adding one of: braille, symbols</li>
<li>U+2821 BRAILLE PATTERN DOTS-16: try adding one of: braille, symbols</li>
<li>U+2822 BRAILLE PATTERN DOTS-26: try adding one of: braille, symbols</li>
<li>U+2823 BRAILLE PATTERN DOTS-126: try adding one of: braille, symbols</li>
<li>U+2824 BRAILLE PATTERN DOTS-36: try adding one of: braille, symbols</li>
<li>U+2825 BRAILLE PATTERN DOTS-136: try adding one of: braille, symbols</li>
<li>U+2826 BRAILLE PATTERN DOTS-236: try adding one of: braille, symbols</li>
<li>U+2827 BRAILLE PATTERN DOTS-1236: try adding one of: braille, symbols</li>
<li>U+2828 BRAILLE PATTERN DOTS-46: try adding one of: braille, symbols</li>
<li>U+2829 BRAILLE PATTERN DOTS-146: try adding one of: braille, symbols</li>
<li>U+282A BRAILLE PATTERN DOTS-246: try adding one of: braille, symbols</li>
<li>U+282B BRAILLE PATTERN DOTS-1246: try adding one of: braille, symbols</li>
<li>U+282C BRAILLE PATTERN DOTS-346: try adding one of: braille, symbols</li>
<li>U+282D BRAILLE PATTERN DOTS-1346: try adding one of: braille, symbols</li>
<li>U+282E BRAILLE PATTERN DOTS-2346: try adding one of: braille, symbols</li>
<li>U+282F BRAILLE PATTERN DOTS-12346: try adding one of: braille, symbols</li>
<li>U+2830 BRAILLE PATTERN DOTS-56: try adding one of: braille, symbols</li>
<li>U+2831 BRAILLE PATTERN DOTS-156: try adding one of: braille, symbols</li>
<li>U+2832 BRAILLE PATTERN DOTS-256: try adding one of: braille, symbols</li>
<li>U+2833 BRAILLE PATTERN DOTS-1256: try adding one of: braille, symbols</li>
<li>U+2834 BRAILLE PATTERN DOTS-356: try adding one of: braille, symbols</li>
<li>U+2835 BRAILLE PATTERN DOTS-1356: try adding one of: braille, symbols</li>
<li>U+2836 BRAILLE PATTERN DOTS-2356: try adding one of: braille, symbols</li>
<li>U+2837 BRAILLE PATTERN DOTS-12356: try adding one of: braille, symbols</li>
<li>U+2838 BRAILLE PATTERN DOTS-456: try adding one of: braille, symbols</li>
<li>U+2839 BRAILLE PATTERN DOTS-1456: try adding one of: braille, symbols</li>
<li>U+283A BRAILLE PATTERN DOTS-2456: try adding one of: braille, symbols</li>
<li>U+283B BRAILLE PATTERN DOTS-12456: try adding one of: braille, symbols</li>
<li>U+283C BRAILLE PATTERN DOTS-3456: try adding one of: braille, symbols</li>
<li>U+283D BRAILLE PATTERN DOTS-13456: try adding one of: braille, symbols</li>
<li>U+283E BRAILLE PATTERN DOTS-23456: try adding one of: braille, symbols</li>
<li>U+283F BRAILLE PATTERN DOTS-123456: try adding one of: braille, symbols</li>
<li>U+2913 DOWNWARDS ARROW TO BAR: try adding math</li>
<li>U+2940 ANTICLOCKWISE CLOSED CIRCLE ARROW: try adding math</li>
<li>U+2B51 BLACK SMALL STAR: try adding symbols</li>
<li>U+2B52 WHITE SMALL STAR: try adding symbols</li>
<li>U+2BBD BALLOT BOX WITH LIGHT X: try adding symbols</li>
<li>U+2BE8 LEFT HALF BLACK STAR: try adding symbols</li>
<li>U+2BE9 RIGHT HALF BLACK STAR: try adding symbols</li>
<li>U+2BEA STAR WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+2BEB STAR WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+33D1 SQUARE LN: not included in any glyphset definition</li>
<li>U+E0A0 : not included in any glyphset definition</li>
<li>U+E0A1 : not included in any glyphset definition</li>
<li>U+E0A2 : not included in any glyphset definition</li>
<li>U+E0A3 : not included in any glyphset definition</li>
<li>U+E0B0 : not included in any glyphset definition</li>
<li>U+E0B1 : not included in any glyphset definition</li>
<li>U+E0B2 : not included in any glyphset definition</li>
<li>U+E0B3 : not included in any glyphset definition</li>
<li>U+EC00 : not included in any glyphset definition</li>
<li>U+EC01 : not included in any glyphset definition</li>
<li>U+EC02 : not included in any glyphset definition</li>
<li>U+EC03 : not included in any glyphset definition</li>
<li>U+EC07 : not included in any glyphset definition</li>
<li>U+EC08 : not included in any glyphset definition</li>
<li>U+EC09 : not included in any glyphset definition</li>
<li>U+EC0A : not included in any glyphset definition</li>
<li>U+EC25 : not included in any glyphset definition</li>
<li>U+EC26 : not included in any glyphset definition</li>
<li>U+EC27 : not included in any glyphset definition</li>
<li>U+EC28 : not included in any glyphset definition</li>
<li>U+EC2A : not included in any glyphset definition</li>
<li>U+EC2B : not included in any glyphset definition</li>
<li>U+EC2C : not included in any glyphset definition</li>
<li>U+EC2E : not included in any glyphset definition</li>
<li>U+EC2F : not included in any glyphset definition</li>
<li>U+1F319 CRESCENT MOON: not included in any glyphset definition</li>
<li>U+1F327 CLOUD WITH RAIN: try adding symbols</li>
<li>U+1F3E0 HOUSE BUILDING: try adding symbols</li>
<li>U+1F44D THUMBS UP SIGN: try adding symbols</li>
<li>U+1F44E THUMBS DOWN SIGN: try adding symbols</li>
<li>U+1F464 BUST IN SILHOUETTE: not included in any glyphset definition</li>
<li>U+1F4AC SPEECH BALLOON: not included in any glyphset definition</li>
<li>U+1F4BE FLOPPY DISK: not included in any glyphset definition</li>
<li>U+1F4C0 DVD: not included in any glyphset definition</li>
<li>U+1F4C1 FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C2 OPEN FILE FOLDER: not included in any glyphset definition</li>
<li>U+1F4C6 TEAR-OFF CALENDAR: not included in any glyphset definition</li>
<li>U+1F4DE TELEPHONE RECEIVER: not included in any glyphset definition</li>
<li>U+1F4F1 MOBILE PHONE: not included in any glyphset definition</li>
<li>U+1F4F6 ANTENNA WITH BARS: not included in any glyphset definition</li>
<li>U+1F500 TWISTED RIGHTWARDS ARROWS: not included in any glyphset definition</li>
<li>U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS: not included in any glyphset definition</li>
<li>U+1F508 SPEAKER: try adding symbols</li>
<li>U+1F50A SPEAKER WITH THREE SOUND WAVES: try adding symbols</li>
<li>U+1F50D LEFT-POINTING MAGNIFYING GLASS: try adding symbols</li>
<li>U+1F50E RIGHT-POINTING MAGNIFYING GLASS: not included in any glyphset definition</li>
<li>U+1F511 KEY: not included in any glyphset definition</li>
<li>U+1F512 LOCK: try adding symbols</li>
<li>U+1F513 OPEN LOCK: try adding symbols</li>
<li>U+1F5A4 BLACK HEART: try adding symbols</li>
<li>U+1F5C0 FOLDER: try adding symbols</li>
<li>U+1F5C1 OPEN FOLDER: try adding symbols</li>
<li>U+1F5D1 WASTEBASKET: try adding symbols</li>
<li>U+1F5D5 MINIMIZE: try adding symbols</li>
<li>U+1F5D6 MAXIMIZE: try adding symbols</li>
<li>U+1F5D8 CLOCKWISE RIGHT AND LEFT SEMICIRCLE ARROWS: try adding symbols</li>
<li>U+1F5F4 BALLOT SCRIPT X: try adding symbols</li>
<li>U+1F5F5 BALLOT BOX WITH SCRIPT X: try adding symbols</li>
<li>U+1F5F6 BALLOT BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F7 BALLOT BOX WITH BOLD SCRIPT X: try adding symbols</li>
<li>U+1F5F9 BALLOT BOX WITH BOLD CHECK: try adding symbols</li>
<li>U+1F600 GRINNING FACE: not included in any glyphset definition</li>
<li>U+1F601 GRINNING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F60A SMILING FACE WITH SMILING EYES: not included in any glyphset definition</li>
<li>U+1F620 ANGRY FACE: not included in any glyphset definition</li>
<li>U+1F621 POUTING FACE: not included in any glyphset definition</li>
<li>U+1F6C9 BOYS SYMBOL: try adding symbols</li>
<li>U+1F6CA GIRLS SYMBOL: try adding symbols</li>
<li>U+1F6D2 SHOPPING TROLLEY: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 14 | 26 | 340 | 25 | 488 | 0 | 
| 0% | 0% | 2% | 3% | 38% | 3% | 55% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
