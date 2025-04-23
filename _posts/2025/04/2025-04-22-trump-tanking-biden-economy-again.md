---
title: "Trump Is Tanking Biden’s Recovery—Again"
description: "Trump already blew up the economy once. Now he’s back to finish the job."
permalink: /2025/trump-tanking-biden-economy-again
date: 2025-04-22T12:00:00Z
classes: wide
categories:
  - Politics
  - Economics
tags:
  - Trump
  - Biden
  - Economy
excerpt: "Trump already blew up the economy once. Now he’s back to finish the job."
header:
  image: /assets/images/2025/04/trump-tanking-biden-economy-again-2048px.jpg
  overlay_image: /assets/images/2025/04/trump-tanking-biden-economy-again-2048px.jpg
  overlay_filter: rgba(0, 0, 0, 0.2)
  teaser: /assets/images/2025/04/trump-tanking-biden-economy-again-575px.jpg
  og_image: /assets/images/2025/04/trump-tanking-biden-economy-again-2048px.jpg
  caption: "[Original](https://wokedissident/)"
toc: true
published: true
---

If Trump was ever “for the working class,” so was Enron. He inherited a growing economy, juiced it with billionaire tax cuts, then crashed it into a pandemic wall. Biden took the wheel in a pile of economic rubble—**and still rebuilt it faster than any president in modern history**.

By the end of 2024, the U.S. wasn’t just recovering—it was **leading the world**. Jobs up. Wages up. Inflation down. Stocks climbing. But Trump is back. And just months into his second act, **the markets are already flinching**.

You wanted the vibes. You’re getting the volatility.

### ⚡️ TL;DR: The Real Economic Scoreboard

<figure>
  <table style="width:100%; border-collapse: collapse; font-size: 15px;">
    <thead>
      <tr style="background-color:#222222; color:#ffffff;">
        <th style="text-align:left; padding: 10px;">Metric</th>
        <th style="text-align:left; padding: 10px;">Trump 1.0 (2017–2021)</th>
        <th style="text-align:left; padding: 10px;">Biden (2021–2025)</th>
        <th style="text-align:left; padding: 10px;">Trump 2.0 (2025 YTD)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px;">Net Jobs Created</td>
        <td style="padding: 10px;">–2.9 million</td>
        <td style="padding: 10px;">+15.6 million</td>
        <td style="padding: 10px;">+320,000 (Q1)</td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 10px;">Average GDP Growth</td>
        <td style="padding: 10px;">+1.4%</td>
        <td style="padding: 10px;">+3.25%</td>
        <td style="padding: 10px;">+1.6% (Q1 est.)</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Median Real Wages</td>
        <td style="padding: 10px;">+$14 (2017–21)</td>
        <td style="padding: 10px;">+$11 (2021–25)</td>
        <td style="padding: 10px;">–$4 (Q1)</td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 10px;">Inflation (YoY Avg)</td>
        <td style="padding: 10px;">1.9%</td>
        <td style="padding: 10px;">5.4% → 2.4%</td>
        <td style="padding: 10px;">2.6% (Mar)</td>
      </tr>
      <tr>
        <td style="padding: 10px;">S&P 500 Performance</td>
        <td style="padding: 10px;">+69.6%</td>
        <td style="padding: 10px;">+33.9%</td>
        <td style="padding: 10px; color:red;"><strong>–3.2%</strong> (YTD)</td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 10px;">Federal Deficit</td>
        <td style="padding: 10px;">–$3.1T (2020 peak)</td>
        <td style="padding: 10px;">–$1.83T (FY2024)</td>
        <td style="padding: 10px;">Rising again (CBO: $1.9T est.)</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Consumer Sentiment</td>
        <td style="padding: 10px;">Collapsed to 71.8 (2020)</td>
        <td style="padding: 10px;">Recovered to 79.4 (late 2024)</td>
        <td style="padding: 10px;">Down to 73.2 (March 2025)</td>
      </tr>
    </tbody>
  </table>
  <figcaption>
    Source: <a href="https://fred.stlouisfed.org/series/PAYEMS">FRED [2]</a>, 
    <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">FRED [7]</a>, 
    <a href="https://fred.stlouisfed.org/series/LES1252881600Q">FRED [1]</a>, 
    <a href="https://fred.stlouisfed.org/series/CPIAUCSL">FRED [10]</a>, 
    <a href="https://fred.stlouisfed.org/series/SP500">FRED [24]</a>, 
    <a href="https://fred.stlouisfed.org/series/FYFSGDA188S">FRED [17]</a>, 
    <a href="https://fred.stlouisfed.org/series/UMCSENT">FRED [27]</a>, 
    <a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">CBO [19]</a>
  </figcaption>
</figure>

## Real Wages and Job Growth: Trump Talked, Biden Delivered

Trump sold himself as the blue-collar billionaire. But let’s check the receipts.

### Median Real Wages: Who Actually Boosted Pay?

Real wages—the money that actually matters after inflation—**rose under both presidents**, but Biden continued the trend despite a historic inflation spike.

<figure>
  <canvas id="realWagesChart" style="width:100%; height:auto; max-height:400px;"></canvas>
  <figcaption>Median weekly real wages, constant 1982–84 dollars. Source: <a href="https://fred.stlouisfed.org/series/LES1252881600Q">BLS via [1]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('realWagesChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Q1 2017', 'Q1 2018', 'Q1 2019', 'Q1 2020', 'Q1 2021', 'Q1 2022', 'Q1 2023', 'Q1 2024', 'Q4 2024', 'Q1 2025'],
      datasets: [{
        label: 'Median Weekly Real Wages (1982–84 $)',
        data: [349, 354, 358, 360, 363, 367, 370, 376, 378, 374],
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        pointBackgroundColor: '#000',
        borderWidth: 2,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      aspectRatio: 2,
      plugins: {
        title: {
          display: true,
          text: 'Median Real Weekly Wages, 2017–2025',
          font: {
            size: 18
          }
        },
        tooltip: {
          mode: 'index',
          intersect: false
        },
        legend: {
          display: false
        }
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      },
      scales: {
        y: {
          title: {
            display: true,
            text: 'Real Wages ($, 1982–84 dollars)'
          },
          ticks: {
            callback: function(value) {
              return '$' + value;
            }
          },
          beginAtZero: false
        },
        x: {
          title: {
            display: true,
            text: 'Quarter'
          }
        }
      }
    }
  });
</script>

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Quarter</th>
        <th style="text-align:left; padding: 8px;">Median Real Weekly Earnings</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">Q1 2017</td>
        <td style="padding: 8px;">$349</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/LES1252881600Q">[1]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Q1 2021</td>
        <td style="padding: 8px;">$363</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/LES1252881600Q">[1]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">Q4 2024</td>
        <td style="padding: 8px;">$378</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/LES1252881600Q">[1]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Q1 2025</td>
        <td style="padding: 8px;">$374</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/LES1252881600Q">[1]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">Net Change</td>
        <td style="padding: 8px;">Trump: +$14 | Biden: +$11</td>
        <td style="padding: 8px;">—</td>
      </tr>
    </tbody>
  </table>
  <figcaption>Median real wages rose under both, but Biden did it through inflation and supply shocks. Source: <a href="https://fred.stlouisfed.org/series/LES1252881600Q">[1]</a></figcaption>
</figure>

### Job Growth: One Lost Jobs, One Set Records

Let’s kill the “Trump was good for jobs” myth for good.

Trump **left office with fewer jobs than he started with**—the first president since Hoover to do so. Biden? He added over 15.6 million.

<figure>
  <canvas id="jobGrowthChart" style="width:100%; max-width:100%; height:auto; max-height:400px;"></canvas>
  <figcaption>Total nonfarm employment, seasonally adjusted. Source: <a href="https://fred.stlouisfed.org/series/PAYEMS">BLS via [2]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const jobGrowthCtx = document.getElementById('jobGrowthChart').getContext('2d');
  new Chart(jobGrowthCtx, {
    type: 'line',
    data: {
      labels: [
        'Jan 2017', 'Jan 2018', 'Jan 2019', 'Jan 2020', 'Apr 2020', 'Jan 2021',
        'Jan 2022', 'Jan 2023', 'Jan 2024', 'Mar 2025'
      ],
      datasets: [{
        label: 'Total Nonfarm Jobs (millions)',
        data: [145.6, 148.3, 151.2, 152.3, 130.3, 142.7, 149.8, 155.2, 157.3, 158.3],
        borderColor: '#43a047',
        backgroundColor: '#43a047',
        tension: 0.3,
        pointRadius: 5,
        pointHoverRadius: 7,
        fill: false
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: context => `${context.raw.toFixed(1)} million`
          }
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: 'Jobs (Millions)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        }
      }
    }
  });
</script>

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Administration</th>
        <th style="text-align:left; padding: 8px;">Start</th>
        <th style="text-align:left; padding: 8px;">End</th>
        <th style="text-align:left; padding: 8px;">Jobs Change</th>
        <th style="text-align:left; padding: 8px;">Monthly Avg</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">Trump (2017–2021)</td>
        <td style="padding: 8px;">145.6M</td>
        <td style="padding: 8px;">142.7M</td>
        <td style="padding: 8px;">–2.9M</td>
        <td style="padding: 8px;">–59,938</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/PAYEMS">[2]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Biden (2021–2025)</td>
        <td style="padding: 8px;">142.7M</td>
        <td style="padding: 8px;">158.3M</td>
        <td style="padding: 8px;">+15.6M</td>
        <td style="padding: 8px;">+311,960</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/PAYEMS">[2]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">Summary</td>
        <td style="padding: 8px;" colspan="2">Net Difference (Biden vs. Trump)</td>
        <td style="padding: 8px;">+18.5M</td>
        <td style="padding: 8px;">+371,898</td>
        <td style="padding: 8px;">—</td>
      </tr>
    </tbody>
  </table>
  <figcaption>Trump ended with fewer jobs. Biden added more than any modern president. Source: <a href="https://fred.stlouisfed.org/series/PAYEMS">[2]</a></figcaption>
</figure>

## GDP Growth—The Real Economic Pulse

You can meme about gas prices all day, but GDP is where economists look when they want to know if a country is *actually* growing.

Trump’s first few years? Decent, if unspectacular. Then came the cliff: a 30% drop in Q2 2020. Biden? He stepped in mid-disaster, stabilized the ship, and delivered **consistently strong growth** even while battling global inflation, war shocks, and a Fed hell-bent on raising rates.

### Annual Real GDP Growth Rates

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Year</th>
        <th style="text-align:left; padding: 8px;">Trump (%)</th>
        <th style="text-align:left; padding: 8px;">Biden (%)</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">2017</td>
        <td style="padding: 8px;">+2.3</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">2018</td>
        <td style="padding: 8px;">+3.0</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">2019</td>
        <td style="padding: 8px;">+2.5</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">2020</td>
        <td style="padding: 8px;">–2.2</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">2021</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;">+5.8</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">2022</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;">+1.9</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">2023</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;">+2.5</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">2024</td>
        <td style="padding: 8px;">—</td>
        <td style="padding: 8px;">+2.8</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">Average</td>
        <td style="padding: 8px;">+1.4%</td>
        <td style="padding: 8px;">+3.25%</td>
        <td style="padding: 8px;">—</td>
      </tr>
    </tbody>
  </table>
  <figcaption>Biden’s 4-year average GDP growth outpaced Trump’s, even with a global economic hangover. Source: <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></figcaption>
</figure>

### Quarterly Chaos: Trump’s Pandemic Cliff Dive

<figure>
  <canvas id="gdpQuarterlyChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Quarterly GDP growth (SAAR %): from Trump’s collapse to Biden’s recovery. Source: <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const gdpCtx = document.getElementById('gdpQuarterlyChart').getContext('2d');
  new Chart(gdpCtx, {
    type: 'bar',
    data: {
      labels: [
        'Q1 2017', 'Q2 2018', 'Q4 2019', 'Q2 2020', 'Q3 2020',
        'Q1 2021', 'Q2 2021', 'Q1 2022', 'Q3 2023', 'Q4 2024'
      ],
      datasets: [{
        label: 'Quarterly Real GDP Growth (SAAR %)',
        data: [1.6, 3.5, 3.5, -29.9, 34.3, 6.0, 7.0, -1.7, 4.9, 2.4],
        backgroundColor: function(context) {
          const value = context.raw;
          return value >= 0 ? 'rgba(30, 136, 229, 0.8)' : 'rgba(229, 57, 53, 0.8)';
        },
        borderColor: '#333',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.raw > 0 ? '+' : ''}${ctx.raw}%`
          }
        },
        legend: { display: false },
        title: {
          display: true,
          text: 'Quarterly Real GDP Growth (Seasonally Adjusted Annual Rate)',
          font: {
            size: 18
          }
        }
      },
      scales: {
        y: {
          title: {
            display: true,
            text: 'Growth Rate (%)'
          },
          ticks: {
            callback: value => `${value}%`
          }
        },
        x: {
          title: {
            display: true,
            text: 'Quarter'
          }
        }
      }
    }
  });
</script>

| Quarter | Real GDP Growth (SAAR %) | President | Source |
|---------|--------------------------|-----------|--------|
| Q2 2020 | –29.9% | Trump | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |
| Q3 2020 | +34.3% | Trump | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |
| Q1 2021 | +6.0% | Biden | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |
| Q2 2021 | +7.0% | Biden | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |
| Q3 2023 | +4.9% | Biden | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |
| Q4 2024 | +2.4% | Biden | <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">[7]</a> |

> “Trump’s economy hit a wall. Biden built a new road.”

## Inflation Panic & Deficit Lies

MAGA talking point #1: “Inflation was low under Trump!”

Sure, if you ignore that he **left office during a global demand crash**, and **ran trillion-dollar deficits in peacetime** before COVID even hit.

Inflation did spike under Biden—but that’s only half the story. The other half? **It’s now lower than when Trump’s economy was flatlining**, and wages are finally rising faster than prices again.

### Inflation Timeline: Pandemic Spike, Global Surge, Steady Decline

<figure>
  <canvas id="inflationTrendChart" style="width:100%; max-width:100%; height:auto; max-height:400px;"></canvas>
  <figcaption>Inflation (CPI & Core CPI) peaked in mid-2022, now near Fed target. Source: <a href="https://fred.stlouisfed.org/series/CPIAUCSL">[10]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const inflationCtx = document.getElementById('inflationTrendChart').getContext('2d');
  new Chart(inflationCtx, {
    type: 'line',
    data: {
      labels: [
        'Jan 2017', 'Jan 2018', 'Jan 2019', 'Jan 2020', 'Jan 2021',
        'Jan 2022', 'Jul 2022', 'Jan 2023', 'Jul 2023', 'Jan 2024', 'Jul 2024', 'Mar 2025'
      ],
      datasets: [
        {
          label: 'CPI (Headline)',
          data: [2.1, 2.1, 1.5, 2.5, 1.4, 7.5, 9.1, 6.4, 3.2, 2.8, 3.1, 2.4],
          borderColor: 'rgba(244, 67, 54, 1)',
          backgroundColor: 'rgba(244, 67, 54, 0.1)',
          tension: 0.3,
          borderWidth: 2,
          pointRadius: 4
        },
        {
          label: 'Core CPI',
          data: [2.2, 2.1, 2.0, 2.3, 1.7, 6.1, 6.7, 5.9, 4.1, 3.8, 3.5, 2.8],
          borderColor: 'rgba(33, 150, 243, 1)',
          backgroundColor: 'rgba(33, 150, 243, 0.1)',
          tension: 0.3,
          borderWidth: 2,
          pointRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'U.S. Inflation Trends: CPI vs Core CPI (2017–2025)',
          font: {
            size: 18
          }
        },
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: context => `${context.dataset.label}: ${context.raw.toFixed(1)}%`
          }
        },
        legend: {
          position: 'top'
        }
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: 'Inflation Rate (%)'
          },
          ticks: {
            callback: val => val + '%'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        }
      }
    }
  });
</script>

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Administration</th>
        <th style="text-align:left; padding: 8px;">CPI-U (Avg %)</th>
        <th style="text-align:left; padding: 8px;">Core CPI-U (Avg %)</th>
        <th style="text-align:left; padding: 8px;">PCE (Avg %)</th>
        <th style="text-align:left; padding: 8px;">Core PCE (Avg %)</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">Trump (2017–2020)</td>
        <td style="padding: 8px;">~1.9%</td>
        <td style="padding: 8px;">~2.0%</td>
        <td style="padding: 8px;">~1.7%</td>
        <td style="padding: 8px;">~1.7%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/CPIAUCSL">[10][11][12]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Biden (2021–Mar 2025)</td>
        <td style="padding: 8px;">~5.4%</td>
        <td style="padding: 8px;">~4.7%</td>
        <td style="padding: 8px;">~4.5%</td>
        <td style="padding: 8px;">~3.9%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/CPIAUCSL">[10][11][12]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">Latest (Mar 2025)</td>
        <td style="padding: 8px;">+2.4%</td>
        <td style="padding: 8px;">+2.8%</td>
        <td style="padding: 8px;">+2.5%</td>
        <td style="padding: 8px;">+2.8%</td>
        <td style="padding: 8px;"><a href="https://www.bls.gov/news.release/cpi.htm">BLS [14]</a></td>
      </tr>
    </tbody>
  </table>
  <figcaption>Inflation surged after global shutdowns, then normalized as supply chains recovered. Source: <a href="https://fred.stlouisfed.org/series/CPIAUCSL">[10]</a></figcaption>
</figure>

### The Federal Deficit: Who Really Blew the Budget?

Trump exploded the deficit **before COVID** with the 2017 tax cuts. Then the pandemic hit, and both parties spent big. But the idea that Biden inherited a balanced budget? Laughable.

And under Trump 2.0? **It’s already widening again.**

<figure>
  <canvas id="deficitChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Deficits as % of GDP ballooned under Trump, shrunk under Biden, now rising again. Source: <a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const deficitCtx = document.getElementById('deficitChart').getContext('2d');
  new Chart(deficitCtx, {
    type: 'bar',
    data: {
      labels: [
        'FY2017', 'FY2018', 'FY2019', 'FY2020', 'FY2021', 
        'FY2022', 'FY2023', 'FY2024', 'FY2025 (proj.)'
      ],
      datasets: [{
        label: 'Deficit as % of GDP',
        data: [-3.4, -3.8, -4.6, -14.7, -11.7, -5.3, -6.1, -6.3, -6.2],
        backgroundColor: function(context) {
          const val = context.raw;
          if (val <= -10) return 'rgba(198, 40, 40, 0.8)';
          if (val <= -5) return 'rgba(255, 111, 0, 0.8)';
          return 'rgba(255, 202, 40, 0.8)';
        },
        borderColor: '#000',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'Federal Deficit as % of GDP (FY2017–FY2025)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.raw.toFixed(1)}% of GDP`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Deficit (% of GDP)'
          },
          ticks: {
            callback: value => `-${value}%`
          },
          suggestedMin: 0,
          suggestedMax: 16,
          reverse: true
        },
        x: {
          title: {
            display: true,
            text: 'Fiscal Year'
          }
        }
      }
    }
  });
</script>

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Fiscal Year</th>
        <th style="text-align:left; padding: 8px;">Deficit ($B)</th>
        <th style="text-align:left; padding: 8px;">Deficit (% GDP)</th>
        <th style="text-align:left; padding: 8px;">Public Debt (% GDP)</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">FY2017</td>
        <td style="padding: 8px;">–$666B</td>
        <td style="padding: 8px;">–3.4%</td>
        <td style="padding: 8px;">75.6%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">FY2020</td>
        <td style="padding: 8px;">–$3.13T</td>
        <td style="padding: 8px;">–14.7%</td>
        <td style="padding: 8px;">100.1%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">FY2021</td>
        <td style="padding: 8px;">–$2.78T</td>
        <td style="padding: 8px;">–11.7%</td>
        <td style="padding: 8px;">97.8%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">FY2024</td>
        <td style="padding: 8px;">–$1.83T</td>
        <td style="padding: 8px;">–6.3%</td>
        <td style="padding: 8px;">97.1%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">FY2025 (proj.)</td>
        <td style="padding: 8px;">–$1.9T</td>
        <td style="padding: 8px;">–6.2%</td>
        <td style="padding: 8px;">Rising again</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
    </tbody>
  </table>
  <figcaption>Trump ran deficits in boom years. Biden reduced them during recovery. Trump 2.0? Already reversing it. Source: <a href="https://fred.stlouisfed.org/series/FYFSGDA188S">[17]</a></figcaption>
</figure>

## Wall Street’s Verdict? Trump’s Back, and It’s Nervous

Markets don’t vote red or blue—they vote green. And when Trump re-entered the White House in January 2025, the market didn’t throw a parade. It tightened its sphincter.

The **S&P 500** has dropped **3.2%** since inauguration day. The **Dow?** Down too. Investors are skittish, the bond market’s flashing warning signs, and volatility is creeping back.

Compare that to the **33.9% gain** under Biden and you see the shift. Loud talk and bad trade policy don’t inspire confidence. Stability does.

### S&P 500 and Dow Performance: Who Really Made You Money?

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Administration</th>
        <th style="text-align:left; padding: 8px;">Index</th>
        <th style="text-align:left; padding: 8px;">Start</th>
        <th style="text-align:left; padding: 8px;">End</th>
        <th style="text-align:left; padding: 8px;">% Change</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">Trump (2017–2021)</td>
        <td style="padding: 8px;">S&P 500</td>
        <td style="padding: 8px;">2,271.31</td>
        <td style="padding: 8px;">3,851.85</td>
        <td style="padding: 8px;">+69.6%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/SP500">[24]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Trump (2017–2021)</td>
        <td style="padding: 8px;">Dow Jones</td>
        <td style="padding: 8px;">19,827.25</td>
        <td style="padding: 8px;">31,188.38</td>
        <td style="padding: 8px;">+57.3%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/DJIA">[25]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">Biden (2021–2025)</td>
        <td style="padding: 8px;">S&P 500</td>
        <td style="padding: 8px;">3,851.85</td>
        <td style="padding: 8px;">5,158.20</td>
        <td style="padding: 8px;">+33.9%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/SP500">[24]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Biden (2021–2025)</td>
        <td style="padding: 8px;">Dow Jones</td>
        <td style="padding: 8px;">31,188.38</td>
        <td style="padding: 8px;">38,170.41</td>
        <td style="padding: 8px;">+22.4%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/DJIA">[25]</a></td>
      </tr>
      <tr style="font-weight:bold;">
        <td style="padding: 8px;">Trump 2.0 (2025 YTD)</td>
        <td style="padding: 8px;">S&P 500</td>
        <td style="padding: 8px;">5,328.10</td>
        <td style="padding: 8px;">5,158.20</td>
        <td style="padding: 8px; color:red;">–3.2%</td>
        <td style="padding: 8px;"><a href="https://fred.stlouisfed.org/series/SP500">[24]</a></td>
      </tr>
    </tbody>
  </table>
  <figcaption>Markets surged under Biden. They’re stumbling under Trump—again. Source: <a href="https://fred.stlouisfed.org/series/SP500">[24]</a>, <a href="https://fred.stlouisfed.org/series/DJIA">[25]</a></figcaption>
</figure>

<figure>
  <canvas id="sp500YTDChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>S&P 500 YTD: Market dropped 3.2% in Trump’s first 3 months back. Source: <a href="https://fred.stlouisfed.org/series/SP500">[24]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const sp500Ctx = document.getElementById('sp500YTDChart').getContext('2d');
  new Chart(sp500Ctx, {
    type: 'line',
    data: {
      labels: [
        'Jan 2', 'Jan 15', 'Feb 1', 'Feb 15', 'Mar 1', 'Mar 15', 'Apr 1', 'Apr 21'
      ],
      datasets: [{
        label: 'S&P 500 Index Level',
        data: [5328.10, 5250.35, 5195.80, 5142.22, 5100.15, 5080.77, 5105.92, 5158.20],
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        tension: 0.4,
        pointRadius: 4,
        pointHoverRadius: 6,
        borderWidth: 2,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: "S&P 500 YTD – Jan to Apr 2025 (Trump 2.0 Era)",
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `Index: ${ctx.raw.toFixed(2)}`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          title: {
            display: true,
            text: 'S&P 500 Index Level'
          },
          beginAtZero: false
        },
        x: {
          title: {
            display: true,
            text: 'Date (2025)'
          }
        }
      }
    }
  });
</script>

## The Tax Scam—Trump Took Care of the Billionaires

Trump called it the “biggest tax cut in history.” He was half right—it was **massive**. But it wasn’t for you.

The **2017 Tax Cuts and Jobs Act** slashed corporate tax rates permanently, threw temporary breadcrumbs at the middle class, and handed the top 1% a golden shovel to bury inequality even deeper.

Meanwhile, most of the individual tax cuts **expire after 2025**. Corporate cuts? Permanent. Funny how that works.

### Who Benefited from the TCJA?

Here’s what happened to **average federal tax rates** by income group, according to the Congressional Budget Office’s post-TCJA analysis [19]:

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Income Group</th>
        <th style="text-align:left; padding: 8px;">Pre-TCJA Avg Tax Rate (%)</th>
        <th style="text-align:left; padding: 8px;">Post-TCJA Avg Tax Rate (%)</th>
        <th style="text-align:left; padding: 8px;">Change (pp)</th>
        <th style="text-align:left; padding: 8px;">Source</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">Lowest Quintile</td>
        <td style="padding: 8px;">1.2%</td>
        <td style="padding: 8px;">0.8%</td>
        <td style="padding: 8px;">–0.4</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Second Quintile</td>
        <td style="padding: 8px;">5.3%</td>
        <td style="padding: 8px;">4.5%</td>
        <td style="padding: 8px;">–0.8</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">Middle Quintile</td>
        <td style="padding: 8px;">9.4%</td>
        <td style="padding: 8px;">8.3%</td>
        <td style="padding: 8px;">–1.1</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Fourth Quintile</td>
        <td style="padding: 8px;">13.9%</td>
        <td style="padding: 8px;">12.6%</td>
        <td style="padding: 8px;">–1.3</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
      <tr>
        <td style="padding: 8px;">Top Quintile</td>
        <td style="padding: 8px;">22.9%</td>
        <td style="padding: 8px;">20.5%</td>
        <td style="padding: 8px;">–2.4</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">Top 1%</td>
        <td style="padding: 8px;">32.4%</td>
        <td style="padding: 8px;">28.6%</td>
        <td style="padding: 8px;">–3.8</td>
        <td style="padding: 8px;"><a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></td>
      </tr>
    </tbody>
  </table>
  <figcaption>Trump’s tax cuts helped everyone a little—but helped the top 1% **a lot**. Source: <a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">[19]</a></figcaption>
</figure>

### Champagne for the 1%, Crumbs for Everyone Else

<figure style="width:100%; max-height:500px; overflow:hidden;">
  <canvas id="tcjaPieChart" style="width:100%; height:auto;"></canvas>
  <figcaption>Distribution of tax cut benefits from TCJA. Top earners took the biggest slice. Source: <a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">CBO [19]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('tcjaPieChart').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: [
          'Lowest Quintile',
          'Second Quintile',
          'Middle Quintile',
          'Fourth Quintile',
          'Top Quintile (Excl. Top 1%)',
          'Top 1%'
        ],
        datasets: [{
          label: 'Tax Cut Share (%)',
          data: [1, 5, 10, 15, 35, 34],
          backgroundColor: [
            '#c8e6c9',
            '#a5d6a7',
            '#81c784',
            '#66bb6a',
            '#43a047',
            '#2e7d32'
          ],
          borderColor: '#fff',
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          title: {
            display: true,
            text: 'Who Benefited from the 2017 Trump Tax Cuts?',
            font: {
              size: 18
            }
          },
          tooltip: {
            callbacks: {
              label: ctx => `${ctx.label}: ${ctx.raw}%`
            }
          },
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 20,
              padding: 10
            }
          }
        }
      }
    });
  });
</script>

> “Trump cut your taxes? Cool. Until 2026, when yours expire—and Jeff Bezos’s don’t.”

## Borders, Crime, and Culture War Bait

If you can’t win on jobs, wages, or growth, scream about “open borders” and “trans athletes.”

That’s been the GOP playbook since facts stopped working for them. But here’s the kicker: **border crossings surged under both Trump and Biden**, crime data is too messy to draw simple lines, and no one’s 401(k) was wrecked by a drag show.

### Border Encounters: A Bipartisan Surge

Border “encounters” hit **record levels under Biden**, yes—but the rise **started under Trump**, and it’s a global trend. Migration exploded post-COVID due to economic instability, climate disasters, and cartel-driven chaos. Biden ended **Title 42**, which artificially suppressed numbers with quick expulsions that didn’t count as deportations.

<figure>
  <canvas id="borderEncountersChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Southwest border encounters rose sharply after pandemic disruptions. Source: <a href="https://www.cbp.gov/newsroom/stats/southwest-land-border-encounters">CBP (External)</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const borderCtx = document.getElementById('borderEncountersChart').getContext('2d');
  new Chart(borderCtx, {
    type: 'bar',
    data: {
      labels: [
        'FY2017', 'FY2018', 'FY2019', 'FY2020', 
        'FY2021', 'FY2022', 'FY2023', 'FY2024'
      ],
      datasets: [{
        label: 'Southwest Border Encounters (millions)',
        data: [0.303, 0.397, 0.851, 0.458, 1.73, 2.38, 2.06, 2.05],
        backgroundColor: function(ctx) {
          const year = ctx.chart.data.labels[ctx.dataIndex];
          return year.startsWith('FY202') ? 'rgba(25, 118, 210, 0.8)' : 'rgba(239, 83, 80, 0.8)';
        },
        borderColor: '#333',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'U.S. Southwest Border Encounters by Fiscal Year (FY2017–FY2024)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.raw.toFixed(2)} million`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Encounters (millions)'
          },
          ticks: {
            callback: val => val + 'M'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Fiscal Year'
          }
        }
      }
    }
  });
</script>

<figure>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#222222;">
        <th style="text-align:left; padding: 8px;">Fiscal Year</th>
        <th style="text-align:left; padding: 8px;">Encounters</th>
        <th style="text-align:left; padding: 8px;">Title 42 in Effect?</th>
        <th style="text-align:left; padding: 8px;">President</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px;">FY2017</td>
        <td style="padding: 8px;">~303,000</td>
        <td style="padding: 8px;">No</td>
        <td style="padding: 8px;">Trump</td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">FY2019</td>
        <td style="padding: 8px;">~851,000</td>
        <td style="padding: 8px;">No</td>
        <td style="padding: 8px;">Trump</td>
      </tr>
      <tr>
        <td style="padding: 8px;">FY2021</td>
        <td style="padding: 8px;">~1.73M</td>
        <td style="padding: 8px;">Yes (until May 2023)</td>
        <td style="padding: 8px;">Biden</td>
      </tr>
      <tr style="background-color:#444444;">
        <td style="padding: 8px;">FY2022</td>
        <td style="padding: 8px;">~2.38M</td>
        <td style="padding: 8px;">Yes</td>
        <td style="padding: 8px;">Biden</td>
      </tr>
      <tr>
        <td style="padding: 8px;">FY2023</td>
        <td style="padding: 8px;">~2.06M</td>
        <td style="padding: 8px;">Yes (ended mid-year)</td>
        <td style="padding: 8px;">Biden</td>
      </tr>
    </tbody>
  </table>
  <figcaption>Encounters surged post-2020 under both parties—Trump started the trend, Biden inherited it. Source: CBP (External)</figcaption>
</figure>

### Crime Trends: FBI Data Is a Wreck

Want to talk about crime? Cool—then let’s talk about **how broken the national data is**.

The FBI transitioned from the old Summary Reporting System (SRS) to NIBRS in 2021. As a result, **40% of law enforcement agencies didn’t report in 2021–2022**, making national comparisons a statistical dumpster fire.

Here’s what we *can* say:

- **Homicides spiked** in 2020–2021 (pandemic + unrest)
- **Property crime kept declining**
- **Biden’s DOJ increased funding for local law enforcement**
- Most “crime surge” narratives are **based on cherry-picked local anecdotes**

<figure>
  <canvas id="homicideRateChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Homicide spike in 2020 wasn’t unique to the U.S.—but it was largest under Trump. Source: FBI UCR (External)</figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const homicideCtx = document.getElementById('homicideRateChart').getContext('2d');
  new Chart(homicideCtx, {
    type: 'line',
    data: {
      labels: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Homicide Rate (per 100k)',
        data: [5.3, 5.0, 5.0, 7.8, 6.9, 6.3, 5.9],
        borderColor: 'rgba(244, 67, 54, 1)',
        backgroundColor: 'rgba(244, 67, 54, 0.2)',
        pointRadius: 5,
        pointHoverRadius: 7,
        borderWidth: 2,
        tension: 0.3,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'U.S. Homicide Rate (2017–2023)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.raw} per 100,000 people`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Homicides per 100k'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Year'
          }
        }
      }
    }
  });
</script>

> “You know what kills more Americans than migrants? Fentanyl. Know who increased funding for that fight? Biden.”

### Interlude: The “Woke” Freakout Is a Copout

Let me guess: you’re “just asking questions” about why girls can’t win track meets anymore, and you’re sick of “woke” stuff like *cancel culture* and *kids being confused about gender*.

Here’s a tip: when someone shouts “woke!”—**they’ve run out of economic arguments.**

You say you’re mad about “trans kids changing sexes”? Cool. Then explain why **the economy collapsed in 2020**. Or why **Trump added $8 trillion to the debt**. Or why **he lost more jobs than any president since the Great Depression**.

Spoiler: **a nonbinary seventh grader didn’t crash your retirement fund**.

And as for “men dominating women’s sports”? Show us the league tables. One-off viral clips aren’t policy arguments. They’re culture war clickbait—**fed to you by people who hope you won’t look at the Fed's balance sheet.**

We get it. “Woke” is your safe word when reality feels threatening.

But this blog isn’t a safe space. Here, we bring **data, not dog whistles.**

### TL;DR:

- **Border encounters surged under both Trump and Biden**
- **Crime spiked in 2020 and started falling by 2023**
- **FBI crime data is incomplete post-2021**
- **Your economic problems weren’t caused by a nonbinary teen at a swim meet**

## Education, Defense & Public Mood

Economic numbers matter. But how people **feel** about the economy is political gold. And under Biden, even through inflation and war shocks, **sentiment began recovering**. Schools were reopening. Wages were outpacing inflation. People started breathing again.

Then Trump came back—and **consumer sentiment dropped like a stone**.

### Education: COVID Wrecked It, Biden Stabilized It

- NAEP scores dropped significantly after 2020.
- Funding per student **increased**, thanks to federal pandemic aid passed under *both* Trump and Biden.
- Long-term trends in math and reading were already stagnating before the pandemic. COVID just hit *fast-forward*.

<figure>
  <canvas id="naepScoreChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Student achievement dropped sharply during pandemic disruption. Source: NCES / NAEP (External)</figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const naepCtx = document.getElementById('naepScoreChart').getContext('2d');
  new Chart(naepCtx, {
    type: 'line',
    data: {
      labels: ['2017', '2019', '2022'],
      datasets: [{
        label: 'NAEP Math Score (Grade 8)',
        data: [282, 280, 271],
        borderColor: 'rgba(33, 150, 243, 1)',
        backgroundColor: 'rgba(33, 150, 243, 0.2)',
        pointRadius: 5,
        pointHoverRadius: 7,
        borderWidth: 2,
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'NAEP Math Scores (Grade 8, National Average)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `Score: ${ctx.raw}`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          suggestedMin: 260,
          suggestedMax: 290,
          title: {
            display: true,
            text: 'Score'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Year'
          }
        }
      }
    }
  });
</script>

> “Trump closed schools, Biden reopened them. Now they blame CRT for the learning gap.”

### Military Spending: Same Money, Different Priorities

- Trump increased the Pentagon’s budget—but **undermined NATO, botched Syria**, and gave the Taliban a peace deal.
- Biden kept funding strong—but **actually used diplomacy**, stabilized NATO post-Ukraine, and increased Indo-Pacific alliances.

<figure>
  <canvas id="defenseSpendingChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Military spending stayed high under both presidents—use of force, very different. Source: DoD / CBO (External)</figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const defenseCtx = document.getElementById('defenseSpendingChart').getContext('2d');
  new Chart(defenseCtx, {
    type: 'line',
    data: {
      labels: ['FY2017', 'FY2018', 'FY2019', 'FY2020', 'FY2021', 'FY2022', 'FY2023', 'FY2024'],
      datasets: [{
        label: 'Defense Spending (% of GDP)',
        data: [3.1, 3.2, 3.2, 3.5, 3.3, 3.1, 3.1, 3.0],
        borderColor: 'rgba(255, 152, 0, 1)',
        backgroundColor: 'rgba(255, 152, 0, 0.2)',
        pointRadius: 5,
        pointHoverRadius: 7,
        borderWidth: 2,
        tension: 0.3,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'U.S. Military Spending as % of GDP (FY2017–FY2024)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.raw}% of GDP`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          suggestedMax: 4,
          title: {
            display: true,
            text: 'Defense Spending (% of GDP)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Fiscal Year'
          }
        }
      }
    }
  });
</script>

> “Trump spent billions on missiles. Biden spent billions making allies not hate us.”

### Public Sentiment: The Mood Was Improving—Then Trump Walked In

Using the **University of Michigan’s Index of Consumer Sentiment**, we can track how Americans *felt*:

- 2020: Cratered under Trump during COVID.
- 2021–22: Stayed low under Biden as inflation soared.
- 2023–24: **Steady rebound** as inflation cooled, job growth surged.
- 2025: **Decline resumes** as Trump 2.0 stokes uncertainty.

<figure>
  <canvas id="consumerSentimentChart" style="width:100%; max-width:100%; height:auto; max-height: 400px;"></canvas>
  <figcaption>Americans were feeling better—until January 2025. Source: <a href="https://fred.stlouisfed.org/series/UMCSENT">University of Michigan / FRED [27]</a></figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const sentimentCtx = document.getElementById('consumerSentimentChart').getContext('2d');
  new Chart(sentimentCtx, {
    type: 'line',
    data: {
      labels: [
        'Jan 2017', 'Jan 2018', 'Jan 2019', 'Jan 2020',
        'Jan 2021', 'Jan 2022', 'Jan 2023', 'Jan 2024', 'Mar 2025'
      ],
      datasets: [{
        label: 'Consumer Sentiment Index',
        data: [98.5, 95.0, 91.2, 89.1, 79.0, 67.2, 64.9, 78.1, 71.0],
        borderColor: 'rgba(76, 175, 80, 1)',
        backgroundColor: 'rgba(76, 175, 80, 0.2)',
        pointRadius: 5,
        pointHoverRadius: 7,
        borderWidth: 2,
        tension: 0.3,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'U.S. Consumer Sentiment Index (2017–2025)',
          font: {
            size: 18
          }
        },
        tooltip: {
          callbacks: {
            label: ctx => `Index: ${ctx.raw}`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          suggestedMin: 50,
          suggestedMax: 100,
          title: {
            display: true,
            text: 'Sentiment Index Value'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        }
      }
    }
  });
</script>

> “People don’t need to read GDP charts. They feel whether the economy works. And right now? They’re feeling Trump’s stink again.”

## Trump’s Back—and the Recovery Is Already Bleeding

Trump inherited a growing economy in 2017 and left it in a ditch by 2021—**worse job numbers than Hoover**, exploding deficits, and a stock market in freefall. 

Biden picked up the wreckage and, against *every headwind possible*—pandemic scars, global inflation, war in Ukraine—**rebuilt faster than any modern president**:

- **15.6 million jobs** added  
- **GDP growth more than doubled Trump’s average**  
- **Wages rose even during inflation**  
- **Markets soared**  
- **Inflation? Peaked and cooled**  
- **Deficit? Down nearly 50% from Trump’s peak**

And now?

Trump 2.0 waltzes back into power in January 2025—and within **three damn months**:

- The **S&P 500 drops 3.2%**  
- **Consumer confidence falls**  
- **Bond yields spike**  
- The **deficit widens again**

We’ve seen this movie. It ends with a recession and a bailout for billionaires.

> You don’t need to love Biden. Hell, be mad about the border. Protest student debt. Demand better.  
>  
> But if you think Trump is the working-class savior while handing trillions to the rich, you’ve been conned by a guy who **literally branded his own steaks**.

### Final Thought:

**If Trump really built the economy, why did it collapse the second he had to govern through a crisis?**

Biden stabilized it.

Trump? He’s already screwing it again.

## <a name="sources"></a>Sources

[1] <a href="https://fred.stlouisfed.org/series/LES1252881600Q">Median Real Weekly Earnings – BLS via FRED</a>   
[2] <a href="https://fred.stlouisfed.org/series/PAYEMS">Total Nonfarm Payroll Employment – BLS via FRED</a>   
[7] <a href="https://fred.stlouisfed.org/series/A191RL1Q225SBEA">Real Gross Domestic Product – BEA via FRED</a>   
[10] <a href="https://fred.stlouisfed.org/series/CPIAUCSL">Consumer Price Index for All Urban Consumers – BLS via FRED</a>   
[11] <a href="https://fred.stlouisfed.org/series/PCEPILFE">Core Personal Consumption Expenditures Price Index – BEA via FRED</a>   
[12] <a href="https://fred.stlouisfed.org/series/PCEPI">Personal Consumption Expenditures (PCE) Index – BEA via FRED</a>   
[14] <a href="https://www.bls.gov/news.release/cpi.htm">Consumer Price Index – March 2025 Report – BLS</a>   
[17] <a href="https://fred.stlouisfed.org/series/FYFSGDA188S">Federal Deficit as % of GDP – U.S. Treasury via FRED</a>   
[19] <a href="https://www.cbo.gov/topics/budget/outlook-budget-and-economy">Budget and Economic Outlook – Congressional Budget Office (CBO)</a>   
[24] <a href="https://fred.stlouisfed.org/series/SP500">S&P 500 Index – FRED</a>   
[25] <a href="https://fred.stlouisfed.org/series/DJIA">Dow Jones Industrial Average – FRED</a>   
[27] <a href="https://fred.stlouisfed.org/series/UMCSENT">University of Michigan Consumer Sentiment Index – FRED</a>   

<!--
## AudioTranscript

Trump already blew up the economy once. Now he’s back to finish the job.

If Trump was ever “for the working class,” so was Enron. He inherited a growing economy, juiced it with billionaire tax cuts, and crashed it into a pandemic wall. Biden took over with the country in economic ruins—and still rebuilt it faster than any president in modern history.

By the end of 2024, the U.S. wasn’t just recovering—it was *leading the world*. Jobs were up. Wages were up. Inflation was down. Markets were climbing.

But Trump is back. And just three months into his second act, the economy’s already flinching.

Let’s talk about the scoreboard.

Under Trump’s first term, the economy **lost 2.9 million jobs**. He became the first president since Hoover to leave office with fewer jobs than he started with. Biden? **Added 15.6 million.** That’s a net difference of over **18 million jobs** between them.

GDP growth? Trump averaged **1.4 percent** a year. Biden? **More than double that—3.25 percent.**

Real wages? They rose under both. Trump saw a gain of **$14 per week**, Biden saw **$11**—and that was while fighting off inflation, war, and a pandemic hangover.

Inflation? Sure, it spiked under Biden—peaking at **9 percent in mid-2022**. But by early 2025, it cooled to **2.4 percent**—almost exactly the Fed’s target. Trump’s average inflation rate was lower, around **1.9 percent**, but that came during a global demand crash and spiraling deficits.

Speaking of deficits: Trump blew a **$3.1 trillion hole** in 2020. Biden? By 2024, had it down to **$1.83 trillion**. Under Trump 2.0? **Already climbing again.**

Markets? The S&P 500 rose nearly **70 percent** under Trump’s first term. It grew **34 percent** under Biden. But since Trump returned in January 2025, the market’s dropped **3.2 percent**—in just three months.

Consumer confidence? It cratered in 2020 under Trump, **rebounded under Biden**, then **dropped again** when Trump returned.

Now let’s talk about the tax cuts.

Trump’s 2017 Tax Cuts and Jobs Act handed the top 1 percent the biggest slice—**a 3.8 percentage point cut** in their effective tax rate. Meanwhile, the bottom fifth of earners got **less than half a point**. Oh, and most middle-class cuts expire after 2025. Corporate cuts? Permanent.

At the border, encounters surged under both Trump and Biden. The real spike began in 2019, jumped post-COVID, and kept rising due to global migration pressures. Biden ended Title 42. Trump built memes, not solutions.

Crime? Yes, homicides spiked—but the peak was in 2020, on Trump’s watch. Rates have dropped since. Property crime kept falling. And FBI data since 2021 has been unreliable anyway, because nearly half of agencies didn’t report.

So when you hear someone blame Biden for every mugging, ask them if they also blame him for your uncle’s cholesterol.

Education? COVID wrecked schools. But Biden re-opened them and stabilized funding. Test scores dropped, yes—but that decline was a global trend, not a partisan failure.

Defense spending? Stayed high under both. But Trump undercut NATO and gave the Taliban a peace deal. Biden kept the budget—and restored America’s alliances.

And how people feel? That’s political gold.

Consumer sentiment nosedived under Trump in 2020, climbed slowly under Biden through 2024, then dropped sharply once Trump returned in 2025. You don’t need to read GDP charts to know the economy’s wobbling. People can feel it.

So here’s the bottom line:

Trump inherited a growing economy in 2017, and by 2021, it was in the ditch. Biden pulled it out—through a pandemic, inflation shocks, and global instability—and still rebuilt faster than any modern president.

And now? Trump 2.0 returns in January 2025—and within three months:

- The S&P 500 drops 3.2 percent  
- Consumer confidence slides  
- The federal deficit starts rising again  

We’ve seen this movie before. It ends with a recession and a bailout for billionaires.

You don’t have to love Biden. Protest him. Pressure him. Demand better.

But if you still believe Trump’s some working-class savior while he’s handing trillions to the rich and tanking the market in real time—you’ve been conned by a guy who literally tried to sell you branded steaks.

Here’s a simple question:

**If Trump built the economy, why did it collapse the second he had to govern through crisis?**

Biden stabilized it.

Trump? He’s already screwing it again.
-->
