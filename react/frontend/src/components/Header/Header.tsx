import { HeaderContainer, Logo } from "./Header.style";


const   Header = () => {
    return (
        <HeaderContainer>
            <div>
                <Logo src="/images/skate-girl.png"/>
            </div>

            <p>Encontre a skatista perfeita!</p>
        </HeaderContainer>
    )
}

export default Header;