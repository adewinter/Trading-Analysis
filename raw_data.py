__author__ = 'adewinter'


KIO_STRING = """

<html><head><title>Financial Summary</title><link rel='stylesheet' href='./ssgeneral.css' type='text/css'><script language='javascript'>function OpenGlossaryForm(Type)		{			if (Type == 0) {			win = window.open('Glossary.asp','Glossary','toolbar=no,status=no,scrollbars=yes,location=no,menubar=no,directories=no,width=420,height=470,resizable=no');}		else {			rptIncome.submit();			} 	}</script></head><body><form name=rptIncome action='Financials.asp?ticker=KIO&action=Export' id=rptIncome method=post><a name='top'><table border=0 width='100%'><tr><td rowspan='2' class='mainheader' width='30%'><img src='images/LogoNew.gif' align='left' /></td><td class='mainheader' width='40%'>Financial Summary</td><td rowspan='2' class='mainheader' width='30%'><img src='images/LogoNew.gif' align='right' /></td></tr><tr><td class='mainheader'>KUMBA IRON ORE LIMITED</td></tr></table><br /><table class='viewexport' border='0' width='100%'><tr><td align=left><a href='javascript:OpenGlossaryForm(0)'><b>View Glossary</b></a></td><td align=right>&nbsp;</td></tr><tr><td colspan=2><hr></td></tr></table><br /><a name='ares'><table width='100%' ><tr class='rowheader'>
<td><B>Year</B></td>
<td align='right'>2010</td>
<td align='right'>2009</td>
<td align='right'>2008</td>
</tr>
<tr class='sheetheader'>
<td><i>Months Covered</i></td>
<td align='right'>12</td>
<td align='right'>12</td>
<td align='right'>12</td>
</tr>
<tr class='sheetheader'>
<td><I>Year End Month</I></td>
<td align='right'>December</td>
<td align='right'>December</td>
<td align='right'>December</td>
</tr>
<tr class='rowheader'><td><b>Ratios</b></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr >
<td>Return on total assets</td>
<td align='right'>0.00</td>
<td align='right'>73.94</td>
<td align='right'>81.82</td>
</tr>
<tr >
<td>Return on equity</td>
<td align='right'>0.00</td>
<td align='right'>95.78</td>
<td align='right'>105.09</td>
</tr>
<tr >
<td>Current Ratio</td>
<td align='right'>0.00</td>
<td align='right'>2.58</td>
<td align='right'>1.75</td>
</tr>
<tr >
<td>Quick Ratio</td>
<td align='right'>2.37</td>
<td align='right'>2.58</td>
<td align='right'>1.75</td>
</tr>
<tr >
<td>Total assets / Turnover</td>
<td align='right'>0.00</td>
<td align='right'>1.31</td>
<td align='right'>1.28</td>
</tr>
<tr >
<td>Debt / Assets</td>
<td align='right'>0.00</td>
<td align='right'>0.34</td>
<td align='right'>0.35</td>
</tr>
<tr >
<td>Debt / Equity</td>
<td align='right'>0.00</td>
<td align='right'>0.84</td>
<td align='right'>0.85</td>
</tr>
<tr class='rowheader'><td><b>Income Statement (000's)</b></td><td align='right'>ZAR</td><td align='right'>ZAR</td><td align='right'>ZAR</td></tr>
<tr >
<td>Turnover</td>
<td align='right'>38,704,000</td>
<td align='right'>23,408,000</td>
<td align='right'>21,360,000</td>
</tr>
<tr >
<td>Earnings Before Interest & Tax (EBIT)</td>
<td align='right'>25,244,000</td>
<td align='right'>13,166,000</td>
<td align='right'>13,667,000</td>
</tr>
<tr >
<td>Interest & Finance Charges</td>
<td align='right'>178,000</td>
<td align='right'>413,000</td>
<td align='right'>405,000</td>
</tr>
<tr >
<td>Taxation</td>
<td align='right'>6,813,000</td>
<td align='right'>3,949,000</td>
<td align='right'>4,179,000</td>
</tr>
<tr >
<td>Profit Attributable To Ordinary Shareholders</td>
<td align='right'>14,287,000</td>
<td align='right'>6,975,000</td>
<td align='right'>7,208,000</td>
</tr>
<tr >
<td>Extra Ordinary Items</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Dividends Paid</td>
<td align='right'>6,756,000</td>
<td align='right'>6,478,000</td>
<td align='right'>3,819,000</td>
</tr>
<tr >
<td>Retained Earnings-current Year</td>
<td align='right'>7,531,000</td>
<td align='right'>497,000</td>
<td align='right'>3,389,000</td>
</tr>
<tr >
<td>Headline Earnings Per Share</td>
<td align='right'>446.7</td>
<td align='right'>218.2</td>
<td align='right'>230.2</td>
</tr>
<tr >
<td>Dividends Per Share</td>
<td align='right'>345.0</td>
<td align='right'>146.0</td>
<td align='right'>210.0</td>
</tr>
<tr >
<td>Depreciation</td>
<td align='right'>765,000</td>
<td align='right'>530,000</td>
<td align='right'>332,000</td>
</tr>
<tr >
<td>Audit Fees</td>
<td align='right'>7,000</td>
<td align='right'>7,000</td>
<td align='right'>7,000</td>
</tr>
<tr >
<td>Directors Emoluments</td>
<td align='right'>15,000</td>
<td align='right'>12,000</td>
<td align='right'>10,000</td>
</tr>
<tr >
<td>EPS-Bottom Line</td>
<td align='right'>446.6</td>
<td align='right'>218.8</td>
<td align='right'>228.0</td>
</tr>
<tr >
<td>EPS-Fully Diluted Headline</td>
<td align='right'>445.4</td>
<td align='right'>217.1</td>
<td align='right'>227.5</td>
</tr>
<tr class='rowheader'><td><b>Balance Sheet (000's)</b></td><td align='right'>ZAR</td><td align='right'>ZAR</td><td align='right'>ZAR</td></tr>
<tr >
<td>Ordinary Shareholders Interest</td>
<td align='right'>14,338,000</td>
<td align='right'>7,282,000</td>
<td align='right'>6,859,000</td>
</tr>
<tr >
<td>Total Shareholders Interest</td>
<td align='right'>18,376,000</td>
<td align='right'>8,956,000</td>
<td align='right'>8,506,000</td>
</tr>
<tr >
<td>Long Term Liabilities</td>
<td align='right'>3,185,000</td>
<td align='right'>3,859,000</td>
<td align='right'>977,000</td>
</tr>
<tr >
<td>Capital Employed</td>
<td align='right'>24,505,000</td>
<td align='right'>15,565,000</td>
<td align='right'>11,857,000</td>
</tr>
<tr >
<td>Total Liabilities</td>
<td align='right'>9,499,000</td>
<td align='right'>8,851,000</td>
<td align='right'>8,197,000</td>
</tr>
<tr >
<td>Fixed Assets</td>
<td align='right'>15,866,000</td>
<td align='right'>11,568,000</td>
<td align='right'>7,911,000</td>
</tr>
<tr >
<td>Mining Assets</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Intangible Assets</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Current Assets</td>
<td align='right'>11,077,000</td>
<td align='right'>5,776,000</td>
<td align='right'>8,498,000</td>
</tr>
<tr >
<td>Current Liabilities</td>
<td align='right'>3,370,000</td>
<td align='right'>2,242,000</td>
<td align='right'>4,846,000</td>
</tr>
<tr >
<td>Adjusted Market/Direct Value In Investment</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Total Assets</td>
<td align='right'>27,875,000</td>
<td align='right'>17,807,000</td>
<td align='right'>16,703,000</td>
</tr>
<tr class='rowheader'><td><b>Cashflow Statement (000's)</b></td><td align='right'>ZAR</td><td align='right'>ZAR</td><td align='right'>ZAR</td></tr>
<tr >
<td>Cash Ex Operations</td>
<td align='right'>26,315,000</td>
<td align='right'>13,193,000</td>
<td align='right'>14,594,000</td>
</tr>
<tr >
<td>Investment Income</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Other Income</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Decrease/increase Working Capital</td>
<td align='right' class='nega'>(760,000)</td>
<td align='right' class='nega'>(571,000)</td>
<td align='right' class='nega'>(75,000)</td>
</tr>
<tr >
<td>Net Interest Paid/received</td>
<td align='right'>283,000</td>
<td align='right'>287,000</td>
<td align='right'>401,000</td>
</tr>
<tr >
<td>Taxation Paid</td>
<td align='right'>7,031,000</td>
<td align='right'>3,232,000</td>
<td align='right'>4,311,000</td>
</tr>
<tr >
<td>Ordinary Dividend</td>
<td align='right'>8,590,000</td>
<td align='right'>8,248,000</td>
<td align='right'>4,870,000</td>
</tr>
<tr >
<td>Preference Dividend</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr >
<td>Increase/decrease Long-Term Liabilities</td>
<td align='right' class='nega'>(876,000)</td>
<td align='right'>56,000</td>
<td align='right'>328,000</td>
</tr>
<tr >
<td>Change In Share Capital</td>
<td align='right' class='nega'>(117,000)</td>
<td align='right'>72,000</td>
<td align='right'>80,000</td>
</tr>
<tr >
<td>Other (Cash Generated)</td>
<td align='right'>0</td>
<td align='right'>0</td>
<td align='right'>0</td>
</tr>
<tr class='rowheader'><td><b>Sundry Statement (000's)</b></td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr >
<td>Nr of Ordinary Shares in Issue @ Year End</td>
<td align='right'>321,912</td>
<td align='right'>320,415</td>
<td align='right'>319,461</td>
</tr>
</table><br/><table border='0' width='100%' ><tr><td colspan='100%' align='center'><hr><br />Data provided by <a href='http://www.mcgbfa.com/'>McGregor BFA</a></td></tr></table></form></body></html>
"""