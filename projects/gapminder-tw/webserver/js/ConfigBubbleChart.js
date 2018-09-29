var ConfigBubbleChart = { 
  "state": {
    "entities": {
      "dim": "geo",
      "filter": {
        "geo": {"un_state": true}
      },
      "show": {}
    },
    "entities_colorlegend": {
      "dim": "world_4region"
    },
    "time": {
      "dim": "time"
    },
    "marker": {
      "space": ["entities", "time"],
      "label": {
        "use": "property",
        "which": "name"
      },
      "axis_y": {
        "use": "indicator",
        "which": "life_expectancy_years",
        "zoomedMin": 19,
        "zoomedMax": 86,
        "domainMin": 0,
        "domainMax": 100
      },
      "axis_x": {
        "use": "indicator",
        "scaleType": "log",
        "domainMax": 180000,
        "domainMin": 300,
        "zoomedMax": 150000,
        "zoomedMin": 400,
        "which": "income_per_person_gdppercapita_ppp_inflation_adjusted"
      },
      "size": {
        "use": "indicator",
        "which": "population_total",
        "domainMin": 15,
        "domainMax": 1400000000,
        "scaleType": "linear",
        "allow": {
          "scales": ["linear"]
        }
      },
      "color": {
        "use": "property",
        "which": "world_4region",
        "scaleType": "ordinal",
        "syncModels": ["marker_colorlegend"]
      }
    },
    "marker_colorlegend":{
      "space": ["entities_colorlegend"],
      "opacityRegular": 0.8,
      "opacityHighlightDim": 0.3,
      "label": {
        "use": "property",
        "which": "name"
      },
      "hook_rank": {
        "use": "property",
        "which": "rank"
      },
      "hook_geoshape": {
        "use": "property",
        "which": "shape_lores_svg"
      }
    }
  },
  "ui": {
    "treemenu": {
      "folderStrategyByDataset": {
        "data": "spread",
        "data_wdi": "folder:other_datasets"
      }
    },
    "datawarning": {
      "doubtDomain": [1800, 1950, 2015],
      "doubtRange": [1.0, 0.3, 0.2]
    },
    "chart": {
      "decorations": {
        "enabled": true,
        "xAxisGroups": {
          "income_per_person_gdppercapita_ppp_inflation_adjusted": [
            {"min": null, "max": 2650, "label": "incomegroups/level1"},
            {"min": 2650, "max": 8000, "label": "incomegroups/level2"},
            {"min": 8000, "max": 24200, "label": "incomegroups/level3"},
            {"min": 24200, "max": null, "label": "incomegroups/level4"}
          ]
        }
      }
     },
    "splash": true
  }
};