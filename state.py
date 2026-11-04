print(page.evaluate("() => ({open: document.querySelector('dialog').open, log: window.__log, submitted: !!window.__submitted})"))
