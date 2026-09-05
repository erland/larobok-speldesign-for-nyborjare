local chapter_pattern = "^Kapitel%s+(%d+)%s*:%s*(.+)$"

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match(chapter_pattern)
  if not number then
    return nil
  end

  local content = {
    pandoc.Span({pandoc.Str("Kapitel " .. number)}, pandoc.Attr("", {"chapter-number"})),
    pandoc.LineBreak(),
    pandoc.Span({pandoc.Str(title)}, pandoc.Attr("", {"chapter-title"}))
  }

  local header = pandoc.Header(1, content, el.attr)

  if FORMAT:match("latex") then
    return {
      pandoc.RawBlock("latex", "\\clearpage"),
      header
    }
  end

  return header
end
