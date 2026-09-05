local chapter_pattern = "^Kapitel%s+(%d+)%s*:%s*(.+)$"

local function latex_escape(text)
  local replacements = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["#"] = "\\#",
    ["$"] = "\\$",
    ["%"] = "\\%",
    ["&"] = "\\&",
    ["_"] = "\\_",
    ["^"] = "\\textasciicircum{}",
    ["~"] = "\\textasciitilde{}",
  }
  return (text:gsub(".", function(char)
    return replacements[char] or char
  end))
end

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match(chapter_pattern)
  if not number then
    return nil
  end

  -- PDF needs an explicit short section title so the TOC stays on one line,
  -- while the visible heading can still be rendered as two centered lines.
  if FORMAT:match("latex") then
    local short = latex_escape("Kapitel " .. number .. ": " .. title)
    local visible_title = latex_escape(title)
    local command = table.concat({
      "\\clearpage",
      "\\section[" .. short .. "]{",
      "{\\normalfont\\large Kapitel " .. number .. "}\\\\[0.35em]",
      "{\\Huge\\bfseries " .. visible_title .. "}",
      "}"
    }, "\n")
    return pandoc.RawBlock("latex", command)
  end

  -- EPUB keeps one semantic H1 string for navigation/TOC. CSS makes the two
  -- spans block-level in the chapter body, so the visible heading is two rows
  -- without inserting a line break into the navigation label.
  local content = {
    pandoc.Span({pandoc.Str("Kapitel " .. number)}, pandoc.Attr("", {"chapter-number"})),
    pandoc.Space(),
    pandoc.Span({pandoc.Str(title)}, pandoc.Attr("", {"chapter-title"}))
  }

  local classes = el.classes
  classes:insert("chapter-heading")
  return pandoc.Header(1, content, pandoc.Attr(el.identifier, classes, el.attributes))
end
