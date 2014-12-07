<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Meine Filme</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th style="text-align:left">Poster</th>
        <th style="text-align:left">Titel</th>
        <th style="text-align:left">Erscheinungsdatum</th>
        <th style="text-align:left">Beliebtheit</th>
        <th style="text-align:left">originalTitel</th>
        <th style="text-align:left">Pfad</th>
        <th style="text-align:left">Beliebtkacke</th>
        <th style="text-align:left">Durchschnitt</th>
      </tr>
      <xsl:for-each select="root/file/movie">
      <tr>
        <td><xsl:value-of select="poster_path"/></td>
        <td><xsl:value-of select="title"/></td>
        <td><xsl:value-of select="release_date"/></td>
        <td><xsl:value-of select="popularity"/></td>
        <td><xsl:value-of select="orginal_title"/></td>
        <td><xsl:value-of select="backdrop_path"/></td>
        <td><xsl:value-of select="vote_count"/></td>
        <td><xsl:value-of select="vote_average"/></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>

