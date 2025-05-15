function Note(el)
  -- Default rendering: leave unchanged
  return el
end

function NoteRef(el)
  local label = el.label
  -- Return a literal [^label] text with hyperlink
  return pandoc.Link(
    pandoc.Str("[^" .. label .. "]"),
    "#" .. label,
    "",  -- title
    { class = "footnote-ref" }
  )
end
