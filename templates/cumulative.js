// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plotly.com/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

trace1 = {
  meta: {columnNames: {
      x: 'Date', 
      y: 'Total Cases'
    }}, 
  mode: 'lines', 
  type: 'bar', 
  xsrc: 'TanishT:22:6695c1', 
  x: ['1/20/20', '1/21/20', '1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20', '1/31/20', '2/1/20', '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20', '2/9/20', '2/10/20', '2/11/20', '2/12/20', '2/13/20', '2/14/20', '2/15/20', '2/16/20', '2/17/20', '2/18/20', '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20', '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20', '3/1/20', '3/2/20', '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20', '3/9/20', '3/10/20', '3/11/20', '3/12/20', '3/13/20', '3/14/20', '3/15/20', '3/16/20', '3/17/20', '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20', '3/23/20', '3/24/20'], 
  ysrc: 'TanishT:22:b32a98', 
  y: ['1', '1', '1', '1', '2', '2', '3', '4', '4', '4', '6', '11', '12', '15', '15', '16', '19', '23', '24', '24', '27', '27', '28', '28', '28', '28', '28', '29', '30', '31', '58', '111', '209', '436', '602', '833', '977', '1261', '1766', '2337', '3150', '3736', '4335', '5186', '5621', '6284', '6593', '7041', '7313', '7478', '7513', '7755', '7869', '7979', '8086', '8162', '8236', '8320', '8413', '8565', '8652', '8799', '8961', '8961', '9037'], 
  orientation: 'v'
};
data = [trace1];
layout = {
  title: {text: 'Cumulative Cases in Korea up to 3/24/2020'}, 
  xaxis: {
    side: 'bottom', 
    type: 'category', 
    range: [-0.5, 64.5], 
    title: {text: 'Date'}, 
    anchor: 'y', 
    domain: [0, 1], 
    autorange: true
  }, 
  yaxis: {
    type: 'linear', 
    range: [0, 9512.631578947368], 
    title: {text: 'Number of Cases'}, 
    anchor: 'x', 
    domain: [0, 1], 
    autorange: true
  }, 
  autosize: true, 
  template: {
    data: {
      bar: [
        {
          type: 'bar', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      table: [
        {
          type: 'table', 
          cells: {
            fill: {color: '#EBF0F8'}, 
            line: {color: 'white'}
          }, 
          header: {
            fill: {color: '#C8D4E3'}, 
            line: {color: 'white'}
          }
        }
      ], 
      carpet: [
        {
          type: 'carpet', 
          aaxis: {
            gridcolor: '#C8D4E3', 
            linecolor: '#C8D4E3', 
            endlinecolor: '#2a3f5f', 
            minorgridcolor: '#C8D4E3', 
            startlinecolor: '#2a3f5f'
          }, 
          baxis: {
            gridcolor: '#C8D4E3', 
            linecolor: '#C8D4E3', 
            endlinecolor: '#2a3f5f', 
            minorgridcolor: '#C8D4E3', 
            startlinecolor: '#2a3f5f'
          }
        }
      ], 
      mesh3d: [
        {
          type: 'mesh3d', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      contour: [
        {
          type: 'contour', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          autocolorscale: true
        }
      ], 
      heatmap: [
        {
          type: 'heatmap', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          autocolorscale: true
        }
      ], 
      scatter: [
        {
          type: 'scatter', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      surface: [
        {
          type: 'surface', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      heatmapgl: [
        {
          type: 'heatmapgl', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      histogram: [
        {
          type: 'histogram', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      parcoords: [
        {
          line: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}, 
          type: 'parcoords'
        }
      ], 
      scatter3d: [
        {
          type: 'scatter3d', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scattergl: [
        {
          type: 'scattergl', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      choropleth: [
        {
          type: 'choropleth', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      scattergeo: [
        {
          type: 'scattergeo', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      histogram2d: [
        {
          type: 'histogram2d', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          autocolorscale: true
        }
      ], 
      scatterpolar: [
        {
          type: 'scatterpolar', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      contourcarpet: [
        {
          type: 'contourcarpet', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      scattercarpet: [
        {
          type: 'scattercarpet', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scattermapbox: [
        {
          type: 'scattermapbox', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scatterpolargl: [
        {
          type: 'scatterpolargl', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scatterternary: [
        {
          type: 'scatterternary', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      histogram2dcontour: [
        {
          type: 'histogram2dcontour', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          autocolorscale: true
        }
      ]
    }, 
    layout: {
      geo: {
        bgcolor: 'white', 
        showland: true, 
        lakecolor: 'white', 
        landcolor: 'white', 
        showlakes: true, 
        subunitcolor: '#C8D4E3'
      }, 
      font: {color: '#2a3f5f'}, 
      polar: {
        bgcolor: 'white', 
        radialaxis: {
          ticks: '', 
          gridcolor: '#EBF0F8', 
          linecolor: '#EBF0F8'
        }, 
        angularaxis: {
          ticks: '', 
          gridcolor: '#EBF0F8', 
          linecolor: '#EBF0F8'
        }
      }, 
      scene: {
        xaxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          gridwidth: 2, 
          linecolor: '#EBF0F8', 
          zerolinecolor: '#EBF0F8', 
          showbackground: true, 
          backgroundcolor: 'white'
        }, 
        yaxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          gridwidth: 2, 
          linecolor: '#EBF0F8', 
          zerolinecolor: '#EBF0F8', 
          showbackground: true, 
          backgroundcolor: 'white'
        }, 
        zaxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          gridwidth: 2, 
          linecolor: '#EBF0F8', 
          zerolinecolor: '#EBF0F8', 
          showbackground: true, 
          backgroundcolor: 'white'
        }
      }, 
      title: {x: 0.05}, 
      xaxis: {
        ticks: '', 
        gridcolor: '#EBF0F8', 
        linecolor: '#EBF0F8', 
        automargin: true, 
        zerolinecolor: '#EBF0F8', 
        zerolinewidth: 2
      }, 
      yaxis: {
        ticks: '', 
        gridcolor: '#EBF0F8', 
        linecolor: '#EBF0F8', 
        automargin: true, 
        zerolinecolor: '#EBF0F8', 
        zerolinewidth: 2
      }, 
      ternary: {
        aaxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          linecolor: '#A2B1C6'
        }, 
        baxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          linecolor: '#A2B1C6'
        }, 
        caxis: {
          ticks: '', 
          gridcolor: '#DFE8F3', 
          linecolor: '#A2B1C6'
        }, 
        bgcolor: 'white'
      }, 
      colorway: ['#636efa', '#EF553B', '#00cc96', '#ab63fa', '#19d3f3', '#e763fa', '#fecb52', '#ffa15a', '#ff6692', '#b6e880'], 
      hovermode: 'closest', 
      colorscale: {
        diverging: [['0', '#8e0152'], ['0.1', '#c51b7d'], ['0.2', '#de77ae'], ['0.3', '#f1b6da'], ['0.4', '#fde0ef'], ['0.5', '#f7f7f7'], ['0.6', '#e6f5d0'], ['0.7', '#b8e186'], ['0.8', '#7fbc41'], ['0.9', '#4d9221'], ['1', '#276419']], 
        sequential: [['0', '#0508b8'], ['0.0893854748603352', '#1910d8'], ['0.1787709497206704', '#3c19f0'], ['0.2681564245810056', '#6b1cfb'], ['0.3575418994413408', '#981cfd'], ['0.44692737430167595', '#bf1cfd'], ['0.5363128491620112', '#dd2bfd'], ['0.6256983240223464', '#f246fe'], ['0.7150837988826816', '#fc67fd'], ['0.8044692737430168', '#fe88fc'], ['0.8938547486033519', '#fea5fd'], ['0.9832402234636871', '#febefe'], ['1', '#fec3fe']], 
        sequentialminus: [['0', '#0508b8'], ['0.0893854748603352', '#1910d8'], ['0.1787709497206704', '#3c19f0'], ['0.2681564245810056', '#6b1cfb'], ['0.3575418994413408', '#981cfd'], ['0.44692737430167595', '#bf1cfd'], ['0.5363128491620112', '#dd2bfd'], ['0.6256983240223464', '#f246fe'], ['0.7150837988826816', '#fc67fd'], ['0.8044692737430168', '#fe88fc'], ['0.8938547486033519', '#fea5fd'], ['0.9832402234636871', '#febefe'], ['1', '#fec3fe']]
      }, 
      plot_bgcolor: 'white', 
      paper_bgcolor: 'white', 
      shapedefaults: {
        line: {width: 0}, 
        opacity: 0.4, 
        fillcolor: '#506784'
      }, 
      annotationdefaults: {
        arrowhead: 0, 
        arrowcolor: '#506784', 
        arrowwidth: 1
      }
    }, 
    themeRef: 'PLOTLY_WHITE'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});