/* K'iin Spa & Lounge - main.js (no dependencies except optional EmailJS for sending quotes) */
(function () {
  "use strict";
  var C = window.KIIN;
  var $ = function (s, r) {
    return (r || document).querySelector(s);
  };
  var $$ = function (s, r) {
    return Array.prototype.slice.call(
      (r || document).querySelectorAll(s),
    );
  };
  var reduce = window.matchMedia(
    "(prefers-reduced-motion: reduce)",
  ).matches;
  var desktop = window.matchMedia(
    "(min-width: 1021px)",
  ).matches;
  var money = function (n) {
    n = Math.round(n * 100) / 100;
    return "$" + (n % 1 ? n.toFixed(2) : n);
  };
  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
      }[c];
    });
  };
  var ICON = {
    arrow: "M5 12h14M13 6l6 6-6 6",
    chat: "M4 5h16v11H9l-5 4z",
    close: "M6 6l12 12M18 6L6 18",
    phone:
      "M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z",
    door: "M6 3h12v18H6zM15 12h.01M6 21h12",
  };
  var svg = function (n, c) {
    return (
      '<svg class="' +
      (c || "ic") +
      '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="' +
      ICON[n] +
      '"/></svg>'
    );
  };
  var svcById = function (id) {
    return C.services.filter(function (s) {
      return s.id === id;
    })[0];
  };

  var yr = $("#yr");
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- Header ---------- */
  var header = $(".site-header");
  var onScroll = function () {
    header.classList.toggle("solid", window.scrollY > 40);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, {
    passive: true,
  });
  var burger = $(".burger");
  var closeMenu = function () {
    document.body.classList.remove("menu-open");
    burger.setAttribute("aria-expanded", "false");
  };
  burger.addEventListener("click", function () {
    var o = document.body.classList.toggle("menu-open");
    burger.setAttribute(
      "aria-expanded",
      o ? "true" : "false",
    );
  });
  var subtog = $(".subtog");
  subtog.addEventListener("click", function (e) {
    if (window.innerWidth <= 1020) {
      e.preventDefault();
      subtog.parentNode.classList.toggle("open");
    }
  });
  $$(".nav a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (!a.classList.contains("subtog")) closeMenu();
    });
  });
  $$(".msub a").forEach(function (a) {
    a.addEventListener("click", closeMenu);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenu();
  });

  /* ---------- Scroll reveal (light on mobile, never hides content for long) ---------- */
  var rev = $$("[data-reveal]");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(
      function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -6% 0px" },
    );
    rev.forEach(function (el) {
      io.observe(el);
    });
    setTimeout(function () {
      rev.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight)
          el.classList.add("in");
      });
    }, 1800);
  } else {
    rev.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ---------- Parallax ---------- */
  var par = $$("[data-parallax]");
  if (par.length && !reduce && desktop) {
    var tick = false;
    var run = function () {
      par.forEach(function (el) {
        var f =
          parseFloat(el.getAttribute("data-parallax")) ||
          0.15;
        var r = el.getBoundingClientRect();
        if (r.bottom < 0 || r.top > window.innerHeight)
          return;
        el.style.transform =
          "translate3d(0," +
          (window.scrollY * f).toFixed(1) +
          "px,0)";
      });
      tick = false;
    };
    window.addEventListener(
      "scroll",
      function () {
        if (!tick) {
          tick = true;
          requestAnimationFrame(run);
        }
      },
      { passive: true },
    );
  }

  /* ---------- Counters ---------- */
  $$("[data-count]").forEach(function (el) {
    var target = +el.getAttribute("data-count"),
      suf = el.getAttribute("data-suffix") || "";
    if (reduce || !("IntersectionObserver" in window))
      return;
    var o = new IntersectionObserver(
      function (es) {
        if (!es[0].isIntersecting) return;
        o.disconnect();
        var t0 = performance.now();
        (function step(t) {
          var p = Math.min((t - t0) / 1400, 1);
          el.textContent =
            Math.round(target * (1 - Math.pow(1 - p, 3))) +
            suf;
          if (p < 1) requestAnimationFrame(step);
        })(t0);
      },
      { threshold: 0.6 },
    );
    o.observe(el);
  });

  /* ---------- Hero: opening doors, particles ---------- */
  var hero = $(".hero");
  if (hero) {
    var tog = $(".doors-toggle", hero),
      label = $("span", tog),
      manual = false,
      timer;
    var setDoors = function (open) {
      hero.setAttribute(
        "data-doors",
        open ? "open" : "closed",
      );
      tog.setAttribute(
        "aria-pressed",
        open ? "false" : "true",
      );
      label.textContent = open
        ? "Close the doors"
        : "Open the doors";
    };
    var begin = function () {
      setDoors(true);
      setTimeout(
        function () {
          hero.classList.add("ready");
        },
        reduce ? 0 : 1100,
      );
    };
    if (reduce) {
      hero.setAttribute("data-doors", "open");
      hero.classList.add("ready");
    } else {
      setTimeout(begin, 500);
    }
    tog.addEventListener("click", function () {
      manual = true;
      setDoors(hero.getAttribute("data-doors") !== "open");
    });
    if (!reduce && desktop) {
      timer = setInterval(function () {
        if (
          manual ||
          document.hidden ||
          hero.matches(":focus-within") ||
          hero.querySelector(".qf:hover") ||
          window.scrollY > window.innerHeight * 0.6
        )
          return;
        setDoors(false);
        setTimeout(function () {
          if (!manual) setDoors(true);
        }, 2900);
      }, 22000);
    }
    var cv = $("#dust");
    if (cv && !reduce && desktop) {
      var cx = cv.getContext("2d"),
        W,
        H,
        P = [];
      var size = function () {
        W = cv.width = hero.offsetWidth;
        H = cv.height = hero.offsetHeight;
      };
      size();
      window.addEventListener("resize", size);
      for (var i = 0; i < 38; i++)
        P.push({
          x: Math.random(),
          y: Math.random(),
          r: Math.random() * 1.8 + 0.4,
          s: Math.random() * 0.0004 + 0.00008,
          a: Math.random() * 6,
        });
      (function frame() {
        if (!document.hidden && window.scrollY < H) {
          cx.clearRect(0, 0, W, H);
          P.forEach(function (p) {
            p.y -= p.s * 16;
            p.a += 0.02;
            if (p.y < -0.02) {
              p.y = 1.02;
              p.x = Math.random();
            }
            cx.beginPath();
            cx.fillStyle =
              "rgba(224,196,138," +
              (0.25 + Math.sin(p.a) * 0.2).toFixed(2) +
              ")";
            cx.arc(
              p.x * W + Math.sin(p.a) * 14,
              p.y * H,
              p.r,
              0,
              6.3,
            );
            cx.fill();
          });
        }
        requestAnimationFrame(frame);
      })();
    }
  }

  /* ---------- Quote helpers ---------- */
  function calcQuote(ids, addIds, guests, tipPct) {
    var lines = [],
      sub = 0,
      mins = 0;
    ids.forEach(function (id) {
      var s = svcById(id);
      if (!s) return;
      var qty = s.pair ? 1 : guests,
        amt = s.price * qty;
      lines.push({
        name: s.name,
        qty: qty,
        amt: amt,
        note: s.pair
          ? "for two"
          : guests > 1
            ? guests + " guests"
            : "",
      });
      sub += amt;
      mins += s.mins;
    });
    addIds.forEach(function (id) {
      var a = C.addons.filter(function (x) {
        return x.id === id;
      })[0];
      if (!a) return;
      var amt = a.price * guests;
      lines.push({
        name: a.name,
        qty: guests,
        amt: amt,
        note: guests > 1 ? guests + " guests" : "",
      });
      sub += amt;
    });
    var tax = sub * (C.taxRate || 0),
      tip = sub * (tipPct / 100);
    return {
      lines: lines,
      sub: sub,
      tax: tax,
      tip: tip,
      total: sub + tax + tip,
      mins: mins,
    };
  }
  function delay(ms) {
    return new Promise(function (r) {
      setTimeout(r, ms);
    });
  }
  function emailReady() {
    var k = C.emailjs;
    return (
      window.emailjs &&
      k &&
      k.publicKey &&
      !/YOUR_/.test(k.publicKey) &&
      !/YOUR_/.test(k.serviceId) &&
      !/YOUR_/.test(k.templateId) &&
      !/example\.com/.test(C.business.ownerEmail)
    );
  }
  function sendMail(params) {
    if (!emailReady()) {
      return delay(900).then(function () {
        return { demo: true };
      });
    }
    var k = C.emailjs;
    window.emailjs.init({ publicKey: k.publicKey });
    var toClient = Object.assign({}, params, {
      to_email: params.client_email,
      to_name: params.client_name,
      audience: "client",
    });
    var toOwner = Object.assign({}, params, {
      to_email: C.business.ownerEmail,
      to_name: "K'iin Spa team",
      audience: "owner",
    });
    return window.emailjs
      .send(k.serviceId, k.templateId, toOwner)
      .then(function () {
        return params.client_email
          ? window.emailjs.send(
              k.serviceId,
              k.templateId,
              toClient,
            )
          : null;
      })
      .then(function () {
        return { demo: false };
      });
  }
  function quoteParams(q, d) {
    var id =
      "KIIN-" +
      Date.now().toString(36).toUpperCase().slice(-6);
    var rows = q.lines
      .map(function (l) {
        return (
          '<tr><td style="padding:6px 0">' +
          esc(l.name) +
          (l.note
            ? ' <span style="color:#888">(' +
              esc(l.note) +
              ")</span>"
            : "") +
          '</td><td style="text-align:right">' +
          money(l.amt) +
          "</td></tr>"
        );
      })
      .join("");
    var text = q.lines
      .map(function (l) {
        return (
          "- " +
          l.name +
          (l.note ? " (" + l.note + ")" : "") +
          ": " +
          money(l.amt)
        );
      })
      .join("\n");
    var html =
      '<table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif">' +
      rows +
      '<tr><td style="border-top:1px solid #ccc;padding-top:8px"><b>Estimated total</b></td><td style="border-top:1px solid #ccc;padding-top:8px;text-align:right"><b>' +
      money(q.total) +
      "</b></td></tr></table>";
    return {
      quote_id: id,
      client_name: d.name,
      client_email: d.email,
      client_phone: d.phone,
      preferred_date: d.date || "",
      preferred_time: d.time || "",
      guests: String(d.guests || 1),
      notes: d.notes || "",
      quote_text: text,
      quote_html: html,
      total: money(q.total),
      duration: q.mins + " min",
      subject: "Your K'iin Spa & Lounge quote " + id,
    };
  }

  /* ---------- Date/time helpers ---------- */
  var today = new Date();
  today.setMinutes(
    today.getMinutes() - today.getTimezoneOffset(),
  );
  var iso = today.toISOString().slice(0, 10);
  $$("input[type=date]").forEach(function (i) {
    i.min = iso;
  });
  function fillTimes(sel) {
    sel.innerHTML =
      '<option value="">Choose a time</option>' +
      C.slots
        .map(function (t) {
          return "<option>" + t + "</option>";
        })
        .join("");
  }

  /* ---------- Hero quick quote ---------- */
  var qf = $("#heroQuote");
  if (qf) {
    var form = $("form", qf),
      steps = $$(".qs", qf),
      bars = $$(".qf-prog i", qf),
      cur = 0,
      cat = null;
    var next = $("[data-next]", qf),
      back = $("[data-back]", qf),
      sel = form.svc;
    fillTimes(form.time);
    var estimate = function () {
      var s = svcById(sel.value);
      var g = +form.guests.value;
      $("[data-est]", qf).textContent = s
        ? money(calcQuote([s.id], [], g, 0).total)
        : "$0";
    };
    var go = function (n) {
      cur = n;
      steps.forEach(function (s, i) {
        s.hidden = i !== n;
      });
      bars.forEach(function (b, i) {
        b.classList.toggle("on", i <= n);
      });
      back.hidden = n === 0;
      next.textContent =
        n === 2 ? "Send my free quote" : "Continue";
    };
    go(0);
    $$(".qchip", qf).forEach(function (b) {
      b.addEventListener("click", function () {
        $$(".qchip", qf).forEach(function (x) {
          x.classList.remove("on");
        });
        b.classList.add("on");
        cat = b.getAttribute("data-cat");
        var list =
          cat === "couples-pick"
            ? C.services.filter(function (s) {
                return s.id === "couples";
              })
            : C.services.filter(function (s) {
                return s.cat === cat;
              });
        sel.innerHTML = list
          .map(function (s) {
            return (
              '<option value="' +
              s.id +
              '">' +
              esc(s.name) +
              " (" +
              s.mins +
              " min) - " +
              money(s.price) +
              "</option>"
            );
          })
          .join("");
        if (cat === "couples-pick") form.guests.value = "2";
        estimate();
        setTimeout(function () {
          next.click();
        }, 260);
      });
    });
    sel.addEventListener("change", estimate);
    form.guests.addEventListener("change", estimate);
    var err = function (m) {
      $$(".qerr", qf)[cur].textContent = m || "";
    };
    back.addEventListener("click", function () {
      err();
      go(cur - 1);
    });
    next.addEventListener("click", function () {
      err();
      if (cur === 0) {
        if (!cat)
          return err(
            "Please choose a service to continue.",
          );
        estimate();
        return go(1);
      }
      if (cur === 1) {
        if (!form.date.value)
          return err("Please pick a date.");
        if (!form.time.value)
          return err("Please pick a time.");
        estimate();
        return go(2);
      }
      var d = {
        name: form.fullname.value.trim(),
        email: form.email.value.trim(),
        phone: form.phone.value.trim(),
        date: form.date.value,
        time: form.time.value,
        guests: +form.guests.value,
      };
      if (!d.name) return err("Please enter your name.");
      if (!/^\S+@\S+\.\S+$/.test(d.email))
        return err("Please enter a valid email address.");
      if (d.phone.replace(/\D/g, "").length < 7)
        return err("Please enter a phone number.");
      var q = calcQuote([sel.value], [], d.guests, 0);
      next.disabled = true;
      next.textContent = "Sending...";
      sendMail(quoteParams(q, d))
        .then(function () {
          form.hidden = true;
          $(".qdone", qf).hidden = false;
          $(".qf-prog", qf).style.display = "none";
        })
        .catch(function () {
          next.disabled = false;
          next.textContent = "Send my free quote";
          err(
            "We could not send that. Please try again or call us.",
          );
        });
    });
  }

  /* ---------- Booking wizard ---------- */
  var bk = $("#bk");
  if (bk) {
    var bf = $("form", bk),
      bsteps = $$(".bs", bk),
      dots = $$(".steps li", bk),
      bc = 0;
    var bnext = $("[data-next]", bk),
      bback = $("[data-back]", bk),
      berr = $(".berr", bk);
    var picked = [],
      addp = [];
    var pick = $(".pick", bk);
    pick.innerHTML = C.categories
      .map(function (c) {
        return (
          '<h3 id="cat-' +
          c.id +
          '">' +
          esc(c.name) +
          "</h3>" +
          C.services
            .filter(function (s) {
              return s.cat === c.id;
            })
            .map(function (s) {
              return (
                '<label class="opt"><input type="checkbox" name="svc" value="' +
                s.id +
                '"><span><b>' +
                esc(s.name) +
                "</b><small>" +
                esc(s.desc) +
                " " +
                s.mins +
                ' min.</small></span><span class="pp">' +
                money(s.price) +
                (s.pair ? "<small> /pair</small>" : "") +
                "</span></label>"
              );
            })
            .join("")
        );
      })
      .join("");
    $(".addpick", bk).innerHTML = C.addons
      .map(function (a) {
        return (
          '<label class="opt"><input type="checkbox" name="add" value="' +
          a.id +
          '"><span><b>' +
          esc(a.name) +
          '</b></span><span class="pp">+' +
          money(a.price) +
          "</span></label>"
        );
      })
      .join("");
    fillTimes(bf.time);
    var qs = new URLSearchParams(location.search);
    if (qs.get("service")) {
      var pre = $(
        'input[name=svc][value="' +
          qs.get("service") +
          '"]',
        bk,
      );
      if (pre) pre.checked = true;
    }
    if (qs.get("cat")) {
      var h = document.getElementById(
        "cat-" + qs.get("cat"),
      );
      if (h)
        setTimeout(function () {
          h.scrollIntoView({
            behavior: "smooth",
            block: "center",
          });
        }, 600);
    }
    var state = function () {
      return {
        ids: $$("input[name=svc]:checked", bk).map(
          function (i) {
            return i.value;
          },
        ),
        adds: $$("input[name=add]:checked", bk).map(
          function (i) {
            return i.value;
          },
        ),
        guests: +bf.guests.value || 1,
        tip: +(bf.tip.value || 0),
      };
    };
    var render = function () {
      var s = state(),
        q = calcQuote(s.ids, s.adds, s.guests, s.tip);
      $(".ql", document).innerHTML = q.lines.length
        ? q.lines
            .map(function (l) {
              return (
                "<li><b>" +
                esc(l.name) +
                (l.note
                  ? " <small>(" + esc(l.note) + ")</small>"
                  : "") +
                "</b><span>" +
                money(l.amt) +
                "</span></li>"
              );
            })
            .join("")
        : '<li class="e">Choose a treatment to see your quote.</li>';
      $("[data-sub]").textContent = money(q.sub);
      $("[data-tax]").textContent = money(q.tax);
      $("[data-tip]").textContent = money(q.tip);
      $("[data-tot]").textContent = money(q.total);
      $("[data-dur]").textContent = q.mins + " min";
      $(".tx").hidden = !(C.taxRate > 0);
      $(".tp").hidden = !s.tip;
      return q;
    };
    bf.addEventListener("change", render);
    render();
    var show = function (n) {
      bc = n;
      bsteps.forEach(function (s, i) {
        s.hidden = i !== n;
      });
      dots.forEach(function (d, i) {
        d.classList.toggle("on", i === n);
        d.classList.toggle("dn", i < n);
      });
      bback.hidden = n === 0;
      bnext.textContent =
        n === 4 ? "Confirm and send my quote" : "Continue";
      if (n === 4) review();
      var top =
        bk.getBoundingClientRect().top +
        window.scrollY -
        100;
      if (window.scrollY > top)
        window.scrollTo({
          top: top,
          behavior: reduce ? "auto" : "smooth",
        });
    };
    var data = function () {
      return {
        name: bf.fullname.value.trim(),
        email: bf.email.value.trim(),
        phone: bf.phone.value.trim(),
        date: bf.date.value,
        time: bf.time.value,
        guests: +bf.guests.value,
        notes: bf.notes.value.trim(),
        date2: bf.date2.value,
      };
    };
    var review = function () {
      var d = data(),
        q = render();
      $(".review", bk).innerHTML =
        "<h4>Treatments</h4><p>" +
        q.lines
          .map(function (l) {
            return esc(l.name) + " - " + money(l.amt);
          })
          .join("<br>") +
        "</p><h4>When</h4><p>" +
        esc(d.date) +
        " at " +
        esc(d.time) +
        (d.date2
          ? "<br>Second choice: " + esc(d.date2)
          : "") +
        " for " +
        d.guests +
        " guest" +
        (d.guests > 1 ? "s" : "") +
        "</p><h4>You</h4><p>" +
        esc(d.name) +
        "<br>" +
        esc(d.email) +
        "<br>" +
        esc(d.phone) +
        "</p>" +
        (d.notes
          ? "<h4>Notes</h4><p>" + esc(d.notes) + "</p>"
          : "") +
        "<h4>Estimated total</h4><p><b>" +
        money(q.total) +
        "</b> (" +
        q.mins +
        " min)</p>";
    };
    var bad = function (m) {
      berr.textContent = m || "";
      return !m;
    };
    var valid = function (n) {
      var d = data();
      if (n === 0 && !state().ids.length)
        return bad("Please choose at least one treatment.");
      if (n === 2) {
        if (!d.date)
          return bad("Please choose a preferred date.");
        if (!d.time)
          return bad("Please choose a preferred time.");
      }
      if (n === 3) {
        if (!d.name) return bad("Please enter your name.");
        if (!/^\S+@\S+\.\S+$/.test(d.email))
          return bad("Please enter a valid email address.");
        if (d.phone.replace(/\D/g, "").length < 7)
          return bad("Please enter a phone number.");
        if (!bf.consent.checked)
          return bad("Please tick the box to continue.");
      }
      return bad("");
    };
    bback.addEventListener("click", function () {
      bad("");
      show(bc - 1);
    });
    bnext.addEventListener("click", function () {
      if (!valid(bc)) return;
      if (bc < 4) return show(bc + 1);
      var d = data(),
        s = state(),
        q = calcQuote(s.ids, s.adds, s.guests, s.tip),
        p = quoteParams(q, d);
      bnext.disabled = true;
      bnext.textContent = "Sending your quote...";
      sendMail(p)
        .then(function (r) {
          var done = $("#bookDone");
          $("[data-dn]", done).textContent =
            d.name.split(" ")[0];
          $("[data-qid]", done).textContent = p.quote_id;
          $("[data-de]", done).textContent = d.email;
          if (r.demo) $(".demo", done).hidden = false;
          done.hidden = false;
          document.body.style.overflow = "hidden";
        })
        .catch(function () {
          bnext.disabled = false;
          bnext.textContent = "Confirm and send my quote";
          bad(
            "Something went wrong sending your quote. Please try again or call us.",
          );
        });
    });
    show(0);
  }

  /* ---------- Contact form ---------- */
  var cf = $("#contactForm");
  if (cf) {
    cf.addEventListener("submit", function (e) {
      e.preventDefault();
      var er = $(".berr", cf),
        ok = $(".ok", cf),
        btn = $("button", cf);
      er.textContent = "";
      if (
        !cf.fullname.value.trim() ||
        !/^\S+@\S+\.\S+$/.test(cf.email.value) ||
        !cf.message.value.trim()
      ) {
        er.textContent =
          "Please add your name, a valid email and a message.";
        return;
      }
      btn.disabled = true;
      var p = {
        quote_id: "MSG",
        client_name: cf.fullname.value,
        client_email: cf.email.value,
        client_phone: cf.phone.value,
        preferred_date: "",
        preferred_time: "",
        guests: "",
        notes: cf.message.value,
        quote_text: cf.message.value,
        quote_html: "<p>" + esc(cf.message.value) + "</p>",
        total: "",
        duration: "",
        subject: "New message from " + cf.fullname.value,
      };
      sendMail(p)
        .then(function () {
          ok.hidden = false;
          cf.reset();
          btn.disabled = false;
        })
        .catch(function () {
          btn.disabled = false;
          er.textContent =
            "We could not send that. Please call us instead.";
        });
    });
  }

  /* ---------- Gallery: filter, lightbox, before/after, video ---------- */
  $$(".filters button").forEach(function (b) {
    b.addEventListener("click", function () {
      $$(".filters button").forEach(function (x) {
        x.classList.remove("on");
      });
      b.classList.add("on");
      var f = b.getAttribute("data-f");
      $$(".gal-grid .lb").forEach(function (i) {
        i.classList.toggle(
          "hide",
          f !== "all" && i.getAttribute("data-cat") !== f,
        );
      });
    });
  });
  var lbs = $$(".lb");
  var openLb = function (idx) {
    var list = lbs.filter(function (l) {
        return (
          !l.classList.contains("hide") &&
          l.offsetParent !== null
        );
      }),
      cur = list.indexOf(lbs[idx]);
    var box = document.createElement("div");
    box.className = "lightbox";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.innerHTML =
      '<img alt=""><button class="lb-x" aria-label="Close">' +
      svg("close") +
      '</button><button class="lb-n lb-p" aria-label="Previous">' +
      svg("arrow") +
      '</button><button class="lb-n lb-nx" aria-label="Next">' +
      svg("arrow") +
      "</button>";
    var im = $("img", box),
      set = function () {
        im.src = list[cur].getAttribute("data-full");
      };
    var close = function () {
      box.remove();
      document.removeEventListener("keydown", key);
      document.body.style.overflow = "";
    };
    var key = function (e) {
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") {
        cur = (cur + 1) % list.length;
        set();
      }
      if (e.key === "ArrowLeft") {
        cur = (cur - 1 + list.length) % list.length;
        set();
      }
    };
    box.addEventListener("click", function (e) {
      if (e.target === box || e.target.closest(".lb-x"))
        close();
      var n = e.target.closest(".lb-n");
      if (n) {
        cur =
          (cur +
            (n.classList.contains("lb-nx") ? 1 : -1) +
            list.length) %
          list.length;
        set();
      }
    });
    document.addEventListener("keydown", key);
    document.body.appendChild(box);
    document.body.style.overflow = "hidden";
    set();
    $(".lb-x", box).focus();
  };
  lbs.forEach(function (l, i) {
    l.addEventListener("click", function () {
      openLb(i);
    });
  });
  $$("[data-ba]").forEach(function (b) {
    var r = $("input", b);
    r.addEventListener("input", function () {
      b.style.setProperty("--p", r.value + "%");
    });
  });
  $$(".vid").forEach(function (v) {
    v.addEventListener("click", function () {
      var vd = C.videos[+v.getAttribute("data-video")],
        m = document.createElement("div");
      m.className = "vmodal";
      m.setAttribute("role", "dialog");
      m.setAttribute("aria-modal", "true");
      var inner;
      if (vd.type === "tiktok" && !/PASTE/.test(vd.id))
        inner =
          '<iframe src="https://www.tiktok.com/embed/v2/' +
          encodeURIComponent(vd.id) +
          '" allow="fullscreen; autoplay" title="' +
          esc(vd.title) +
          '"></iframe>';
      else if (vd.type === "mp4" && vd.src)
        inner =
          '<video src="' +
          esc(vd.src) +
          '" controls autoplay playsinline></video>';
      else
        inner =
          '<div class="vmsg"><h3>Add your video</h3><p>Paste your TikTok video ID into js/config.js (or point to an MP4 in assets/video). See the README for the 30-second steps.</p></div>';
      m.innerHTML =
        '<div class="vbox">' +
        inner +
        '</div><button class="lb-x" aria-label="Close video">' +
        svg("close") +
        "</button>";
      var close = function () {
        m.remove();
        document.removeEventListener("keydown", k);
        document.body.style.overflow = "";
      };
      var k = function (e) {
        if (e.key === "Escape") close();
      };
      m.addEventListener("click", function (e) {
        if (e.target === m || e.target.closest(".lb-x"))
          close();
      });
      document.addEventListener("keydown", k);
      document.body.appendChild(m);
      document.body.style.overflow = "hidden";
      $(".lb-x", m).focus();
    });
  });

  /* ---------- Testimonial slider ---------- */
  $$("[data-t]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = $(".ttrack");
      t.scrollBy({
        left:
          +b.getAttribute("data-t") *
          (t.firstElementChild.offsetWidth + 22),
        behavior: "smooth",
      });
    });
  });

  /* ---------- Chat assistant (call and message) ---------- */
  var B = C.business;
  var chat = document.createElement("div");
  chat.innerHTML =
    '<button class="chat-fab" aria-label="Chat, call or message us" aria-expanded="false">' +
    svg("chat") +
    "</button>" +
    '<div class="chat" role="dialog" aria-label="Chat with K\'iin Spa"><div class="chat-h"><img src="assets/img/crest-light.png" alt=""><div><b>K\'iin Concierge</b><small>Ask us anything, or call</small></div><button aria-label="Close chat">' +
    svg("close") +
    "</button></div>" +
    '<div class="chat-act"><a href="tel:' +
    B.phone +
    '">' +
    svg("phone") +
    'Call</a><a href="sms:' +
    B.phone +
    '">' +
    svg("chat") +
    'Text</a><a href="' +
    B.messenger +
    '" target="_blank" rel="noopener">Messenger</a></div>' +
    '<div class="chat-m" aria-live="polite"></div><div class="chat-q"></div><form class="chat-f"><input aria-label="Type your question" placeholder="Type your question..." autocomplete="off"><button aria-label="Send">' +
    svg("arrow") +
    "</button></form></div>";
  document.body.appendChild(chat);
  var fab = $(".chat-fab"),
    panel = $(".chat"),
    msgs = $(".chat-m"),
    quick = $(".chat-q"),
    cform = $(".chat-f");
  var say = function (t, me) {
    var d = document.createElement("div");
    d.className = "msg " + (me ? "me" : "bot");
    d.innerHTML = t;
    msgs.appendChild(d);
    msgs.scrollTop = msgs.scrollHeight;
  };
  var KB = [
    {
      k: /price|cost|how much|rate|quote/,
      a:
        "Prices start at " +
        money(
          Math.min.apply(
            null,
            C.services.map(function (s) {
              return s.price;
            }),
          ),
        ) +
        '. Use our <a href="booking.html">instant quote tool</a> to see your total.',
    },
    {
      k: /book|appoint|schedule|reserve/,
      a:
        'You can book in about a minute on our <a href="booking.html">booking page</a>, or call <a href="tel:' +
        B.phone +
        '">' +
        B.phoneDisplay +
        "</a>.",
    },
    {
      k: /massage|deep|swedish|stone|couple|prenatal/,
      a: 'Our massage menu includes Swedish, deep tissue, hot stone, prenatal and couples. <a href="massage-therapy.html">See massage therapy</a>.',
    },
    {
      k: /facial|skin|peel/,
      a: 'We offer custom facials and gentle peels. <a href="facials-skincare.html">See facials and skincare</a>.',
    },
    {
      k: /hair|cut|color|colour|braid|silk|blowout/,
      a: 'Cuts, colour, silk press, blowouts and protective styles. <a href="hair-salon.html">See the hair salon</a>.',
    },
    {
      k: /nail|mani|pedi|acrylic|gel/,
      a: 'Manicures, pedicures, gel and acrylic. <a href="nails.html">See nails</a>.',
    },
    {
      k: /lash|brow/,
      a: 'Lash sets, fills, lifts and brow shaping. <a href="lashes-brows.html">See lashes and brows</a>.',
    },
    {
      k: /gift|card/,
      a:
        'Gift cards are available <a href="' +
        B.giftCardUrl +
        '" target="_blank" rel="noopener">here</a>.',
    },
    {
      k: /where|address|location|park|direction/,
      a:
        "We are at " +
        B.address +
        '. <a href="contact.html">Get directions</a>.',
    },
    {
      k: /hour|open|close|time/,
      a:
        'We work by appointment. Call <a href="tel:' +
        B.phone +
        '">' +
        B.phoneDisplay +
        "</a> for current hours and availability.",
    },
    {
      k: /hi|hello|hey|good (morning|afternoon|evening)/,
      a: "Hello, and welcome to K'iin Spa & Lounge. How can we help you today?",
    },
  ];
  var reply = function (t) {
    t = t.toLowerCase();
    var hit = KB.filter(function (x) {
      return x.k.test(t);
    })[0];
    say(
      hit
        ? hit.a
        : 'I am not sure about that one. The quickest way to reach a person is to <a href="tel:' +
            B.phone +
            '">call ' +
            B.phoneDisplay +
            '</a> or <a href="sms:' +
            B.phone +
            '">send a text</a>.',
    );
  };
  [
    "Book an appointment",
    "Prices",
    "Services",
    "Gift cards",
    "Location",
  ].forEach(function (q) {
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = q;
    b.addEventListener("click", function () {
      say(q, true);
      setTimeout(function () {
        reply(
          q === "Services"
            ? "massage facial hair nail lash"
            : q === "Book an appointment"
              ? "book"
              : q,
        );
      }, 350);
    });
    quick.appendChild(b);
  });
  cform.addEventListener("submit", function (e) {
    e.preventDefault();
    var i = cform.querySelector("input"),
      v = i.value.trim();
    if (!v) return;
    say(esc(v), true);
    i.value = "";
    setTimeout(function () {
      reply(v);
    }, 450);
  });
  var opened = false,
    toggle = function (o) {
      panel.classList.toggle("open", o);
      fab.setAttribute("aria-expanded", o);
      if (o && !opened) {
        opened = true;
        say(
          "Welcome to K'iin Spa &amp; Lounge. Ask about services, prices or booking, or call us any time on <a href=\"tel:" +
            B.phone +
            '">' +
            B.phoneDisplay +
            "</a>.",
        );
      }
    };
  fab.addEventListener("click", function () {
    toggle(!panel.classList.contains("open"));
  });
  $(".chat-h button").addEventListener(
    "click",
    function () {
      toggle(false);
    },
  );
})();
