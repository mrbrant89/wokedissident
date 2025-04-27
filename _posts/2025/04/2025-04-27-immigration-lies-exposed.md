---
title: "The Immigration Lies You Keep Falling For"
description: "How a delusional MAGA keyboard warrior accidentally exposed the real truth about migrants—and how billionaires are laughing all the way to the bank."
permalink: /2025/immigration-lies-exposed
date: 2025-04-27T15:00:00Z
classes: wide
categories:
  - Politics
  - Immigration
tags:
  - Immigration
  - MAGA
  - Deportation
  - Labor
  - Healthcare
excerpt: "Turns out the dishwasher isn't stealing your healthcare. It's the billionaire dodging taxes while you're busy punching down."
header:
  image: /assets/images/2025/04/immigration-lies-exposed-2048px.jpg
  overlay_image: /assets/images/2025/04/immigration-lies-exposed-2048px.jpg
  overlay_filter: rgba(0, 0, 0, 0.2)
  teaser: /assets/images/2025/04/immigration-lies-exposed-575px.jpg
  og_image: /assets/images/2025/04/immigration-lies-exposed-2048px.jpg
  caption: "[Original](https://wokedissident.com/)"
toc: true
published: true
---

As usual, a delusional MAGA keyboard warrior — furious at the wrong people — is pounding out nonsense on Threads.

Here are a few brain droppings he blessed us with:

> "**We just have to remove the illegals and we'll have free healthcare.**"  
> "**They can go to their own countries and piss on everything like they do here.**"  
> "**They steal, rape, murder, and gangbang on my taxes.**"

You know the type.  

Proudly unemployed, six beers deep by noon, and blaming the dishwasher for why insulin costs $800.

Time to shred this bullshit—backed by actual numbers, not rage emojis.

## Who Are the Migrants, Really?

First, let's demolish the "they're invading us!" nonsense.

- As of January 2025, there are **53.3 million foreign-born residents** in the U.S., about **15.8%** of the total population <a href="#sources">[1]</a>.
- Only about **11 to 13.7 million** are undocumented — **barely 3–4%** of everyone living here <a href="#sources">[2]</a>.
- And guess what? **At least 42%** of the undocumented population *came legally and overstayed a visa* <a href="#sources">[3]</a>.  
  Not border-hopping. Not tunnel-digging. Legally. Through airports. You know, like your uncle on a Spirit Airlines bender to Cancun.

Meanwhile, the "immigrant share" of the population today is still **lower than it was in 1890** <a href="#sources">[4]</a>.  

Yeah. When your great-grandpa showed up drunk off the boat and immediately started a bar fight.

So unless you're mad at Ellis Island too, maybe sit this one out.

<figure>
<canvas id="immigrantPopulationChart" style="max-height: 400px;"></canvas>
<figcaption><strong>Figure 1:</strong> Immigrants make up about 14–15.8% of the U.S. population — depending on the survey. Still close to historic highs. Data: U.S. Census Bureau (ACS 2023, CPS 2025).</figcaption>
</figure>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('immigrantPopulationChart').getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['1890', '2023 (ACS)', '2025 (CPS)'],
        datasets: [{
            label: 'Immigrant Share of U.S. Population (%)',
            data: [14.8, 14.3, 15.8],
            backgroundColor: '#ff4747',
            borderColor: '#ffffff',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            },
            x: {
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            }
        },
        plugins: {
            legend: {
                labels: {
                    color: '#eee'
                }
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.dataset.label + ': ' + context.parsed.y + '%';
                    }
                }
            }
        }
    }
});
</script>

## They Do the Jobs MAGA Won't Touch

Another MAGA myth down the drain:  
> Migrants aren't "stealing jobs" — they're doing the ones you won't even apply for.

- **Service jobs:** 21.8% of foreign-born workers vs. 15% of native-born <a href="#sources">[5]</a>.
- **Construction and maintenance:** 13.8% foreign-born vs. 7.8% native-born <a href="#sources">[5]</a>.
- **Production, transportation, material moving:** 15.2% foreign-born vs. 11.8% native-born <a href="#sources">[5]</a>.

Meanwhile, immigrants are *less likely* to be hanging out in cushy office gigs (13% vs 20.1%).

Also? They make **less money** than native-born workers — about **87 cents on the dollar** <a href="#sources">[6]</a>.

*Translation:*  
> You’re not standing in a strawberry field at 5 AM because you’re too busy tweeting "build the wall" from your heated pickup truck.

<figure>
<canvas id="occupationChart" style="max-height: 400px;"></canvas>
<figcaption><strong>Figure 2:</strong> Immigrants are overrepresented in essential, physically demanding jobs. Data: Bureau of Labor Statistics, 2023.</figcaption>
</figure>

<script>
const ctx2 = document.getElementById('occupationChart').getContext('2d');
new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Service Jobs', 'Construction/Maintenance', 'Production/Transportation', 'Office Jobs'],
        datasets: [
            {
                label: 'Foreign-Born Workers (%)',
                data: [21.8, 13.8, 15.2, 13.0],
                backgroundColor: '#ff4747',
                borderColor: '#ffffff',
                borderWidth: 1
            },
            {
                label: 'Native-Born Workers (%)',
                data: [15.0, 7.8, 11.8, 20.1],
                backgroundColor: '#4747ff',
                borderColor: '#ffffff',
                borderWidth: 1
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            },
            x: {
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            }
        },
        plugins: {
            legend: {
                labels: {
                    color: '#eee'
                }
            }
        }
    }
});
</script>

## Crime: Manufactured Fear

Next myth on the chopping block:  
> Migrants are violent criminals flooding your streets.

Reality check:
- **Native-born Americans:** 1,221 incarcerations per 100,000 people.  
- **Undocumented immigrants:** 613 per 100,000.  
- **Legal immigrants:** 319 per 100,000 <a href="#sources">[7]</a>.

Immigrants — even undocumented ones — are **half as likely** to be locked up as native-born citizens.  

Legal immigrants? *Four times less likely.*

Meanwhile, as immigration *doubled* between 1980 and 2022, **total U.S. crime dropped by 60%** <a href="#sources">[8]</a>.

*But sure, keep clenching your purse when a landscaper walks by. Not like your drunk neighbor with an AR-15 is the real problem.*

<figure>
<canvas id="incarcerationChart" style="max-height: 400px;"></canvas>
<figcaption><strong>Figure 3:</strong> Incarceration Rates per 100,000 Population. Data: Cato Institute analysis of 2023 American Community Survey data.</figcaption>
</figure>

<script>
const ctx3 = document.getElementById('incarcerationChart').getContext('2d');
new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: ['Native-Born', 'Undocumented Immigrants', 'Legal Immigrants'],
        datasets: [{
            label: 'Incarceration Rate per 100,000',
            data: [1221, 613, 319],
            backgroundColor: ['#4747ff', '#ff4747', '#47ff47'],
            borderColor: '#ffffff',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            },
            x: {
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});
</script>

## The Tax Scam: They Pay, You Whine

Here's the part MAGA rage-farmers don’t want you to know:

Undocumented immigrants pay **$96.7 billion** in taxes every year <a href="#sources">[9]</a>.  

That’s an average of nearly **$9,000 per person** — even though half don't even have health insurance.

How it breaks down:

| Tax Type                   | Amount Paid (Billions) |
|:----------------------------|:----------------------|
| Federal Taxes               | $59.4                 |
|  &nbsp; ↳ Social Security    | $25.7                 |
|  &nbsp; ↳ Medicare           | $6.4                  |
|  &nbsp; ↳ Unemployment Ins.  | $1.8                  |
| State & Local Taxes          | $37.3                 |
| &nbsp; ↳ Sales & Excise      | $15.1                 |
| &nbsp; ↳ Property Taxes      | $10.4                 |
| &nbsp; ↳ State Income Taxes  | $7.0                  |

**Table 1:** Undocumented Immigrant Tax Contributions, 2022 (Source: ITEP, Yale Budget Lab)

And guess what?  

They **pay into Social Security**—over **$25.7 billion a year**—but **can't collect benefits** <a href="#sources">[10]</a>.

That money **subsidizes your retirement**, Chad.

And if you deport 1 million of them? Poof. **$8.9 billion** in lost annual tax revenue <a href="#sources">[11]</a>.

But sure, keep thinking they're "freeloaders" while you cash a Social Security check they helped fund.

**Bonus Reality Check:**
> Their **U.S.-born children** (a.k.a. "anchor babies" in MAGA-speak) turn out to be **even bigger net fiscal contributors** than native-born Americans <a href="#sources">[12]</a>.

Meaning: *The kids you want to deport are actually funding the country better than your favorite senator.*

## Healthcare: Deporting Won’t Save You, Genius

Here's another sad trombone moment for MAGA healthcare "experts":
- **50%** of undocumented immigrants are uninsured <a href="#sources">[13]</a>.
- Immigrants — documented *and* undocumented — spend **significantly less** on healthcare than native-born Americans.

How much less?
- Average healthcare spending per immigrant: **$4,875/year**.
- Average for native-born citizens: **$7,277/year** <a href="#sources">[14]</a>.

*Translation:*  
> They're not clogging the system. They're subsidizing it by staying healthy and avoiding the ER—despite getting zero help from the insurance-industrial complex.

<figure>
<canvas id="healthcareSpendingChart" style="max-height: 400px;"></canvas>
<figcaption><strong>Figure 4:</strong> Average Annual Healthcare Expenditures. Data: Kaiser Family Foundation, 2023.</figcaption>
</figure>

<script>
const ctx4 = document.getElementById('healthcareSpendingChart').getContext('2d');
new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: ['Immigrants', 'Native-Born Citizens'],
        datasets: [{
            label: 'Annual Healthcare Spending ($)',
            data: [4875, 7277],
            backgroundColor: ['#ff4747', '#4747ff'],
            borderColor: '#ffffff',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            },
            x: {
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});
</script>

Deporting immigrants **won’t magically fund healthcare**.  

It’ll just:
- **Shrink GDP by up to 6.8%**.
- **Rip $100 billion+ a year** out of Social Security and Medicare.
- **Explode hospital operating losses** (because fewer people will be paying into the system at all).

*You'll still be broke, uninsured, and bleeding out in the ER waiting room — but at least José won't be there holding a mop.*

## The True Cost of Deportations: Spoiler, It’s Trillions
If you think deporting immigrants will "save" the country, buckle up:
- **Direct cost to deport 11 million immigrants:** **$1 trillion** over the next decade <a href="#sources">[16]</a>.
- **Lost tax revenue:** **$8.9 billion** per year — minimum <a href="#sources">[11]</a>.
- **GDP shrinkage:** up to **6.8% annually** <a href="#sources">[16]</a>.

And the human wreckage?  
- Thousands of **U.S. citizen children** (yeah, "anchor babies") **ripped from families**.
- Documented spikes in **child PTSD, depression, chronic illness** after parental deportations <a href="#sources">[17]</a>.

Congratulations, patriot — you wrecked the economy, traumatized a generation, and still didn’t get free healthcare.

<figure>
<canvas id="deportationCostChart" style="max-height: 400px;"></canvas>
<figcaption><strong>Figure 5:</strong> What $1 Trillion Could Actually Fund Instead of Mass Deportation.</figcaption>
</figure>

<script>
const ctx5 = document.getElementById('deportationCostChart').getContext('2d');
new Chart(ctx5, {
    type: 'bar',
    data: {
        labels: [
            '10,000 Gold Toilets for Senators',
            'Space Force Base on the Moon',
            'Healthcare for All Uninsured Americans (10 years)',
            'Nationwide Free Insulin (20+ years)',
            'Expand Medicaid in All 50 States'
        ],
        datasets: [{
            label: 'Cost Estimate ($ Billion)',
            data: [300, 500, 900, 650, 450],
            backgroundColor: '#ff4747',
            borderColor: '#ffffff',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        scales: {
            x: {
                beginAtZero: true,
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            },
            y: {
                ticks: {
                    color: '#eee'
                },
                grid: {
                    color: '#444'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});
</script>

*In other words:*

For what it costs to kick out the dishwasher and the roofer, we could literally:
- Fund **healthcare for every uninsured American** for a decade,
- **Provide free insulin** for everyone who needs it,
- **Expand Medicaid** across all 50 states,
- And still have enough left over for a Space Force moon base and a golden toilet in every senator’s office.

But yeah, let's waste it trying to deport José for the crime of mopping a hospital floor better than you.

## Historical Reality Check: U.S. Meddling Made the Crisis
Funny how the loudest voices screaming about "invaders" never mention *why* people are fleeing in the first place.

Turns out when you:
- Prop up military dictators,
- Stage coups against elected leaders,
- Flood countries with guns and drug money,
- Rig trade deals that crush local economies,

You get desperate people showing up at your door.

The U.S. didn’t just "inherit" this migration crisis.  

**We helped build it** — brick by bloody brick.

**Want the receipts?**  
Check out ["Reagan to Biden: Four Decades of Immigration Chaos"](https://wokedissident.com/2025/reagan-to-biden-immigration) for the full, brutal history.

*Spoiler:*  
It's a hell of a lot uglier than anything you'll hear on Fox News.

## Punch Up, Not Down

The dishwasher isn’t why you can’t afford insulin.  

The roofer isn’t why your kid’s college costs more than your first house.  

The farmworker isn’t why your town lost its hospital.

**You’re broke because billionaires bought your government.**

And while you're busy blaming a Honduran line cook, they’re laughing their way to the Cayman Islands — on money you worked for.

So stop swinging at the guy mopping hospital floors at 2 a.m. **Start swinging at the guy lobbying Congress to cut his taxes to zero.**

Final truth bomb:
> *Blaming immigrants for your problems is like blaming the waiter because the CEO spit in your food.*

**Grow up. Punch up. Or get used to being robbed blind.**

## Sources
<a name="sources"></a>

- [1] <a href="https://usafacts.org/answers/how-many-immigrants-are-in-the-us/country/united-states/">How many immigrants are in the United States? – USAFacts</a>
- [2] <a href="https://www.migrationpolicy.org/article/frequently-requested-statistics-immigrants-and-immigration-united-states">Frequently Requested Statistics on Immigrants and Immigration in the United States – Migration Policy Institute</a>
- [3] <a href="https://cis.org/Camarota/American-Community-Survey-Shows-Record-Size-and-Growth-ForeignBorn-Population-2023">American Community Survey Shows Record Size and Growth in Foreign-Born Population in 2023 – Center for Immigration Studies</a>
- [4] <a href="https://www.cato.org/blog/native-born-americans-are-not-losing-jobs-foreigners">Native-Born Americans Are Not Losing Jobs to Foreigners – Cato Institute</a>
- [5] <a href="https://www.epi.org/publication/u-s-benefits-from-immigration/">The U.S. benefits from immigration but policy reforms needed to maximize gains – Economic Policy Institute</a>
- [6] <a href="https://cis.org/Report/ForeignBorn-Number-and-Share-US-Population-AllTime-Highs-January-2025">Foreign-Born Number and Share of U.S. Population at All-Time Highs in January 2025 – Center for Immigration Studies</a>
- [7] <a href="https://www.migrationpolicy.org/news/us-unauthorized-population-diversifying">Diverse Flows Drive Increase in U.S. Unauthorized Immigrant Population – Migration Policy Institute</a>
- [8] <a href="https://pop.psu.edu/news/mpi-issues-latest-estimates-size-and-origins-us-unauthorized-immigrant-population">MPI Issues Latest Estimates of the Size and Origins of the U.S. Unauthorized Immigrant Population – Social Science Research Institute</a>
- [9] <a href="https://www.cato.org/policy-analysis/illegal-immigrant-incarceration-rates-2010-2023">Illegal Immigrant Incarceration Rates, 2010–2023 – Cato Institute</a>
- [10] <a href="https://www.epi.org/publication/unauthorized-immigrants/">Unauthorized immigrants and the economy – Economic Policy Institute</a>
- [11] <a href="https://www.pewresearch.org/short-reads/2024/11/22/most-americans-say-undocumented-immigrants-should-be-able-to-stay-legally-under-certain-conditions/">Most Americans say undocumented immigrants should be able to stay legally under certain conditions – Pew Research Center</a>
- [13] <a href="https://budgetlab.yale.edu/research/potential-impact-irs-ice-data-sharing-tax-compliance">The Potential Impact of IRS-ICE Data Sharing on Tax Compliance – Yale Budget Lab</a>
- [14] <a href="https://www.congress.gov/crs-product/R47848">Nonimmigrant Overstays: Overview and Policy Issues – Congress.gov</a>
- [16] <a href="https://www.researchgate.net/publication/273512264_Beyond_DAPA_and_DACA_Revisiting_Legislative_Reform_in_Light_of_Long-Term_Trends_in_Unauthorized_Immigration_to_the_United_States">Beyond DAPA and DACA: Revisiting Legislative Reform – ResearchGate</a>
- [17] <a href="https://www.dhs.gov/sites/default/files/2024-10/24_1011_CBP-Entry-Exit-Overstay-Report-FY23-Data.pdf">Entry/Exit Overstay Report – U.S. Department of Homeland Security</a>
- [18] <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11735039/">Beyond Stocks and Surges: The Demographic Impact of the Migration Flow – NIH.gov</a>
- [19] <a href="https://www.migrationpolicy.org/article/central-american-immigrants-united-states">Central American Immigrants in the United States – Migration Policy Institute</a>
- [21] <a href="https://www.unicef.org/innocenti/media/7801/file/UNICEF-Innocenti-Migration-Latin-America-Caribbean-2024.pdf">Research on Child Migration and Displacement in Latin America and the Caribbean – UNICEF</a>
- [22] <a href="https://scholarworks.uvm.edu/cgi/viewcontent.cgi?article=1387&context=hcoltheses">Honduras: Factors Underlying Immigration to the United States – University of Vermont</a>
- [23] <a href="https://www.bls.gov/news.release/forbrn.nr0.htm">Labor Force Characteristics of Foreign-born Workers Summary – Bureau of Labor Statistics</a>
- [25] <a href="https://www.pewtrusts.org/en/research-and-analysis/data-visualizations/2015/immigrant-employment-by-state-and-industry">Immigrant Employment by State and Industry – Pew Charitable Trusts</a>
- [26] <a href="https://www.americanimmigrationcouncil.org/research/mass-deportation">Mass Deportation: Devastating Costs to America – American Immigration Council</a>
- [27] <a href="https://www.kff.org/racial-equity-and-health-policy/issue-brief/potential-impacts-of-mass-detention-and-deportation-efforts-on-the-health-and-well-being-of-immigrant-families/">Potential Impacts of Mass Detention and Deportation Efforts on Health – Kaiser Family Foundation</a>
- [28] <a href="https://www.kff.org/racial-equity-and-health-policy/issue-brief/key-facts-on-health-care-use-and-costs-among-immigrants/">Key Facts on Health Care Use and Costs Among Immigrants – Kaiser Family Foundation</a>
- [29] <a href="https://wol.iza.org/articles/do-migrants-take-the-jobs-of-native-workers/long">Do migrants take the jobs of native workers? – IZA World of Labor</a>
- [33] <a href="https://www.nationalacademies.org/our-work/economic-and-fiscal-impact-of-immigration">Economic and Fiscal Impact of Immigration – National Academies of Sciences</a>
- [34] <a href="https://www.nationalacademies.org/news/2016/09/new-report-assesses-the-economic-and-fiscal-consequences-of-immigration">New Report Assesses the Economic and Fiscal Consequences of Immigration – National Academies of Sciences</a>
- [35] <a href="https://iine.org/2024/04/dispelling-10-common-myths-about-immigrants-and-refugees/">Dispelling 10 Common Myths About Immigrants and Refugees – International Institute of New England</a>
- [36] <a href="https://www.pewresearch.org/topic/immigration-migration/">Immigration & Migration Data – Pew Research Center</a>
- [37] <a href="https://www.brookings.edu/articles/strong-labor-market-boosted-us-born-employment/">Strong Labor Market Boosted US-born Employment – Brookings Institution</a>
- [38] <a href="https://econpapers.repec.org/RePEc:nbr:nberwo:31440">The Incarceration Gap Between Immigrants and the US-born, 1870–2020 – NBER</a>
- [42] <a href="https://www.americanimmigrationcouncil.org/research/debunking-myth-immigrants-and-crime">Debunking the Myth of Immigrants and Crime – American Immigration Council</a>
- [44] <a href="https://valencia.unm.edu/library/handouts/evaluationsources/sanctuaryd.pdf">The Politics of Refuge: Sanctuary Cities and Crime – UNM Valencia</a>
- [45] <a href="https://www.brookings.edu/articles/democracy-in-the-age-of-new-media-a-report-on-the-media-and-the-immigration-debate/">Democracy in the Age of New Media: Immigration Debate – Brookings Institution</a>
- [46] <a href="https://deepblue.lib.umich.edu/bitstream/handle/2027.42/139632/mbcullen.pdf">Deepblue Study on Crime Reporting – University of Michigan</a>
- [47] <a href="https://www.cato.org/blog/why-do-illegal-immigrants-have-low-crime-rate-twelve-explanations">Why Do Illegal Immigrants Have Low Crime Rates? – Cato Institute</a>
- [48] <a href="https://itep.org/study-undocumented-immigrants-contribute-nearly-100-billion-in-taxes-a-year/">Study: Undocumented Immigrants Contribute Nearly $100 Billion in Taxes a Year – Institute on Taxation and Economic Policy</a>
- [53] <a href="https://budgetlab.yale.edu/research/potential-impact-irs-ice-data-sharing-tax-compliance">Potential Impact of IRS-ICE Data Sharing on Tax Compliance – Yale Budget Lab</a>
- [57] <a href="https://www.americanprogress.org/article/improving-lives-strengthening-finances-the-benefits-of-immigration-reform-to-social-security/">The Benefits of Immigration Reform to Social Security – Center for American Progress</a>
- [63] <a href="https://www.cbo.gov/publication/60165">Effects of the Immigration Surge on the Federal Budget and the Economy – Congressional Budget Office</a>
- [64] <a href="https://www.cbo.gov/publication/60569">Further Effects of Immigration Surge on Budget and Economy – Congressional Budget Office</a>
- [67] <a href="https://www.kff.org/racial-equity-and-health-policy/fact-sheet/key-facts-on-health-coverage-of-immigrants/">Key Facts on Health Coverage of Immigrants – Kaiser Family Foundation</a>
- [68] <a href="https://www.congress.gov/crs-product/R47351">Noncitizens' Access to Health Care – Congress.gov</a>
- [70] <a href="https://www.everycrsreport.com/files/2024-11-14_R47351_3679a283b74a5035f770aa35d56770772e1c3341.pdf">Noncitizens' Access to Health Care – Every CRS Report</a>
- [71] <a href="https://www.urban.org/sites/default/files/2024-01/State-Led%20Health%20Insurance%20Coverage%20Expansions%20for%20Noncitizens.pdf">State-Led Health Insurance Coverage Expansions for Noncitizens – Urban Institute</a>
- [72] <a href="https://www.kff.org/racial-equity-and-health-policy/issue-brief/health-coverage-by-race-and-ethnicity/">Health Coverage by Race and Ethnicity – Kaiser Family Foundation</a>
- [75] <a href="https://education.cfr.org/learn/learning-journey/americas-essentials/us-foreign-policy-the-americas">U.S. Foreign Policy: The Americas – Council on Foreign Relations (CFR)</a>
- [77] <a href="https://ccis.ucsd.edu/_files/wp10.pdf">U.S. Relations with Mexico and Central America, 1977-1999 – Center for Comparative Immigration Studies</a>
- [80] <a href="https://www.pewresearch.org/topic/immigration-migration/immigration-issues/unauthorized-immigration/">Unauthorized Immigration – Pew Research Center</a>

<!-- 
## AudioTranscript

As usual, a delusional MAGA keyboard warrior — furious at the wrong people — is pounding out nonsense on Threads.

Here’s what he blessed the world with:

We just have to remove the illegals and we'll have free healthcare.

They can go to their own countries and piss on everything like they do here.

They steal, rape, murder, and gangbang on my taxes.

You know the type. Proudly unemployed, six beers deep by noon, blaming the dishwasher for why insulin costs eight hundred dollars.

Time to shred this bullshit. With real numbers. Not rage emojis.

First, who are the migrants, really?

As of January twenty twenty-five, there are fifty-three million foreign-born residents in the United States. About fifteen point eight percent of the total population.

Only about eleven to thirteen million are undocumented. That’s barely three to four percent of everyone living here.

And guess what. At least forty-two percent of the undocumented came legally and overstayed a visa.
They didn’t border-hop. They didn’t dig tunnels. They flew in through airports. Like your uncle on a Spirit Airlines bender to Cancun.

Meanwhile, the immigrant share of the population today is still lower than it was in eighteen ninety. When your great-grandpa showed up drunk off the boat and immediately started a bar fight.

Unless you’re mad at Ellis Island too, maybe sit this one out.

Next, let’s kill the job-stealing myth.

Migrants aren’t taking your jobs. They’re doing the ones you won’t even apply for.

Service jobs? Twenty-two percent immigrant. Only fifteen percent native-born.

Construction and maintenance? Thirteen point eight percent immigrant. Seven point eight percent native.

Production, transportation, moving? Fifteen percent immigrant. Eleven point eight percent native.

Meanwhile, immigrants are less likely to be in cushy office jobs. And they make less money. About eighty-seven cents on the dollar compared to native-born workers.

Translation. You’re not standing in a strawberry field at five a.m. because you’re too busy tweeting build the wall from your heated pickup truck.

Now, let’s torch the crime panic.

Native-born Americans are incarcerated at twelve hundred twenty-one per hundred thousand people.

Undocumented immigrants? Six hundred thirteen.

Legal immigrants? Three hundred nineteen.

Meaning immigrants — even undocumented ones — are about half as likely to be locked up as native-born citizens.

Legal immigrants? Four times less likely.

Meanwhile, as immigration doubled between nineteen eighty and twenty twenty-two, total U.S. crime dropped by sixty percent.

You’re statistically safer living next to a Honduran dishwasher than next to a sovereign citizen prepper.

Next up, the tax scam nobody talks about.

Undocumented immigrants pay ninety-six point seven billion dollars in taxes every year.
That’s nine thousand bucks each — on average.

They pay into Social Security — twenty-five billion dollars a year — even though they’re barred from collecting benefits.

Their money is literally subsidizing your retirement, Chad.

If you deport a million of them? You blow a nine billion dollar hole in tax revenue every year.

And their U.S.-born kids? They’re even bigger net fiscal contributors than most of the angry keyboard warriors yelling about anchor babies.

Now, about healthcare.

Half of undocumented immigrants are uninsured.

Immigrants spend twenty-four hundred dollars less per year on healthcare than native-born citizens.

They’re not bankrupting the system. They’re barely using it.

And if you deport them? GDP shrinks. Hospitals close. Costs explode.

You’ll still be broke. You’ll still be waiting six hours in the ER. You’ll just be alone.

Now for the real cost of deportations.

Mass deportation would cost over one trillion dollars. Plus another ninety billion in lost tax revenue over ten years.

GDP would shrink up to six point eight percent every year.

And the human carnage? Thousands of U.S. citizen kids ripped from their parents. Kids who develop PTSD, chronic illness, depression, anxiety.

All to chase a fantasy about freeloaders who actually pay more into the system than they take out.

What could we buy with that one trillion dollars instead?

We could fund healthcare for every uninsured American for a decade.

We could give free insulin to every diabetic for twenty years.

We could expand Medicaid nationwide.

Or, if you’re feeling stupid, we could also build a Space Force base on the moon and install ten thousand golden toilets for senators.

Your choice.

And if you want to know why people are fleeing Latin America in the first place, maybe read a history book.
Or better yet, check out my blog post on how the United States spent the last hundred years breaking Latin America.

Spoiler.
When you bankroll death squads, stage coups, flood countries with guns, and crush local economies, you tend to create refugees.

Now. Final word.

The dishwasher isn’t why you can’t afford insulin.

The roofer isn’t why your kid’s college costs more than your first house.

The farmworker isn’t why your town lost its hospital.

You’re broke because billionaires bought your government.

And while you’re busy blaming a migrant picking tomatoes, they’re laughing their asses off, buying their fourth yacht.

Stop punching down.
Start punching up.

Final truth bomb.

Blaming immigrants for your problems is like blaming the waiter because the CEO spit in your food.

Grow up.
Punch up.
Or get used to being robbed blind.
-->